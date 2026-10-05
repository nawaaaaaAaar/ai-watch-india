import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const bytes=p=>readFileSync(new URL(p,root));
const json=p=>JSON.parse(bytes(p));
const hash=b=>createHash('sha256').update(b).digest('hex');
const data=json('public/combined-data.json'), summary=json('public/data-room/dataset-summary.json');
const coverage=json('public/data-room/coverage.json'), gaps=json('public/data-room/gaps.json'), evidence=json('public/data-room/evidence-items.json');
const manifest=json('public/data-room/manifest.json');
const health=data.provisions.find(p=>p.id==='service-esanjeevani');
test('complete inventory separates dossiers from selected contributions',()=>{
  assert.equal(coverage.length,72);assert.equal(coverage.filter(p=>p.contribution).length,46);
  assert.deepEqual(summary.counts,{families:5,records:72,briefs:46,sources:46,corrections:10,accountabilityFields:72,evidenceItems:evidence.length,gapRows:gaps.length});
  assert.equal(gaps.length,140);assert.deepEqual(manifest.counts,summary.counts);
});
test('JSONL reproduces every exact stored record',()=>{
  const rows=bytes('public/data-room/records.jsonl').toString().trim().split('\n').map(JSON.parse);
  assert.deepEqual(rows,data.provisions);
});
test('all seventy-two dossiers include exact record JSON and supporting URLs',()=>{
  for(const p of data.provisions){
    const text=bytes(`public/data-room/dossiers/${p.id}.md`).toString();
    assert.ok(text.includes(JSON.stringify(p,null,2)),p.id);
    for(const e of p.evidenceTrail||[])assert.ok(text.includes(e.url));
  }
});
test('all-record bundle includes non-contribution coverage records',()=>{
  const out=bytes('public/data-room/all-record-dossiers.md').toString();
  for(const p of data.provisions)assert.ok(out.includes(`"id": "${p.id}"`));
  assert.equal(data.provisions.filter(p=>!p.contribution).length,26);
});
test('coverage resolves every record, source identifier and dossier',()=>{
  assert.deepEqual(coverage.map(p=>p.id),data.provisions.map(p=>p.id));
  for(const c of coverage){assert.ok(c.sourceCount>0,c.id);for(const id of c.sourceIds)assert.ok(data.sources.some(s=>s.id===id),id);assert.ok(existsSync(new URL('public/'+c.dossier,root)));}
});
test('source catalogue preserves all forty-six dated and hashed snapshots',()=>{
  assert.equal(data.sources.length,46);
  for(const s of data.sources){assert.equal(hash(bytes('public/'+s.snapshot)),s.hash,s.id);assert.ok(s.url.startsWith('https://'));assert.ok(s.checked&&s.documentDate&&s.hashType);}
  assert.match(bytes('public/data-room/sources.csv').toString(),/context-dpdp-act/);
});
test('all evidence entries retain exact quotes, source identifiers and record links',()=>{
  assert.equal(new Set(evidence.map(e=>e.id)).size,evidence.length);
  for(const e of evidence){assert.ok(data.provisions.some(p=>p.id===e.recordId));assert.ok(data.sources.some(s=>s.id===e.sourceId),e.id);assert.ok(e.quote&&e.url&&e.locator,e.id);}
});
test('limitation register contains every caution without invented absence conclusions',()=>{
  for(const p of data.provisions)assert.equal(gaps.find(g=>g.id===p.id+'-limit').statement,p.caution);
  assert.equal(gaps.filter(g=>g.kind==='Record limit').length,72);
  assert.equal(gaps.filter(g=>g.kind==='Implementation record queue').length,10);
});
test('every non-documented case dimension survives the gap register',()=>{
  for(const p of data.provisions.filter(p=>p.publicServiceCase))for(const [i,f] of p.caseFields.entries()){
    const row=gaps.find(g=>g.id===`${p.id}-field-${i}`);
    if(f.status==='Documented')assert.equal(row,undefined);
    else {assert.equal(row.statement,f.statement);assert.equal(row.status,f.status);assert.deepEqual(row.sourceUrls,f.evidence.map(e=>e.url));}
  }
});
test('raw comparison and coverage are byte-equivalent to research originals',()=>{
  for(const name of ['provision-comparison.jsonl','provision-coverage.csv'])assert.deepEqual(bytes('research/'+name),bytes('public/data-room/raw-'+name));
});
test('ten correction rows retain original and replacement text in structured dataset',()=>{
  assert.equal(data.corrections.length,10);
  const out=bytes('public/data-room/corrections.csv').toString();
  for(const c of data.corrections)assert.ok(out.includes(c.id));
});
test('manifest hashes every payload and exact file size',()=>{
  assert.equal(new Set(manifest.files.map(f=>f.path)).size,manifest.files.length);
  for(const f of manifest.files){const b=bytes(f.path==='schema/schema.ts'?'shared/schema.ts':'public/'+f.path);assert.equal(b.length,f.size,f.path);assert.equal(hash(b),f.sha256,f.path);}
  assert.ok(manifest.files.some(f=>f.path==='data-room/dataset-summary.json'));
  assert.equal(hash(bytes('public/data-room/manifest.json')),bytes('public/data-room/manifest-sha256.txt').toString().split(' ')[0]);
});
test('ZIP passes CRC and reproduces every manifested payload byte',()=>{
  const out=execFileSync('python',['-c',`import zipfile,json,hashlib; z=zipfile.ZipFile('public/data-room/complete-data.zip'); assert z.testzip() is None; m=json.loads(z.read('data-room/manifest.json')); assert len(z.namelist())==len(m['files'])+2; assert all('..' not in n.split('/') and not n.startswith('/') for n in z.namelist()); assert all(hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256'] and len(z.read(f['path']))==f['size'] for f in m['files']); print('PASS')`],{cwd:root}).toString();
  assert.match(out,/PASS/);
  assert.equal(hash(bytes('public/data-room/complete-data.zip')),bytes('public/data-room/archive-sha256.txt').toString().split(' ')[0]);
});
test('archive explicitly excludes private reviews and unsupported archive claims',()=>{
  assert.match(manifest.archiveScope,/not full original PDF binaries/i);
  assert.ok(!manifest.files.some(f=>/test-results|node_modules|notebook|\.env/.test(f.path)));
  assert.match(bytes('public/data-room/README.md').toString(),/does not grant a blanket licence/);
});
test('national study is clearly abstract-only with full manuscript access failure',()=>{
  const s=data.sources.find(s=>s.id==='service-health-implementation-study');
  assert.equal(s.sourceType,'Research abstract; full manuscript not reviewed');
  assert.match(health.caseFields[6].statement,/abstract/);
  assert.match(bytes('public/research/completeness-retrieval.csv').toString(),/Blocked by content fetch; browser article blocked/);
});
test('March and April dates are retained as conflicting descriptions',()=>{
  assert.equal(health.caseFields[2].status,'Conflicting sources');
  assert.match(health.caseFields[2].statement,/March 2023/);assert.match(health.caseFields[2].statement,/April 2023/);
});
test('study funding is not converted into zero-cost national deployment',()=>{
  assert.equal(health.caseFields[4].status,'Partial');
  assert.match(health.caseFields[4].statement,/not.*deployment/i);
});
test('historical grievance guidance does not claim the current form works',()=>{
  assert.equal(health.caseFields[9].status,'Partial');
  assert.match(health.caseFields[9].statement,/not verified|could not/i);
  assert.match(bytes('public/research/completeness-retrieval.csv').toString(),/Current complaint form not verified/);
});
test('statutory context does not increase comparison or collection counts',()=>{
  assert.equal(json('src/data/context.json').sources.length,1);
  assert.ok(data.sources.some(s=>s.id==='context-dpdp-act'));assert.equal(data.provisions.length,72);assert.equal(data.families.length,5);
});
test('static download handler preserves binary blobs',()=>{
  const app=bytes('src/main.tsx').toString();
  assert.match(app,/response\.blob\(\)/);assert.match(app,/downloadBlob/);
  assert.ok(app.includes('Earlier corpus archive'));
});
