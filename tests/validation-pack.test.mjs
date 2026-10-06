import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url),base=new URL('../public/validation/',import.meta.url);
const json=f=>JSON.parse(fs.readFileSync(f.startsWith('manager/')?new URL(`private-validation/${f}`,root):new URL(f,base)));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const inv=json('inventory.json'),sources=json('reviewer/sources.json');
function python(code){return execFileSync('python',['-c',code],{cwd:root}).toString();}
test('validation keeps 144 systems and ten implementation families',()=>{
 assert.equal(inv.system_count,144);assert.equal(inv.cases,10);assert.equal(inv.independent_review_completed,false);
 assert.equal(JSON.parse(fs.readFileSync(new URL('public/registry/data.json',root))).systems.length,144);
});
test('605 existing public files and fourteen app sources are byte preserved',()=>{
 const b=JSON.parse(fs.readFileSync(new URL('research/validation/baseline-fixed.json',root)));
 assert.equal(b.files.length,619);for(const f of b.files)assert.equal(hash(fs.readFileSync(new URL(f.path,root))),f.sha256,f.path);
 assert.equal(b.files.filter(f=>f.path.startsWith('src/')).length,14);
});
test('review includes six task types with 316 units and 992 assignments',()=>{
 assert.equal(inv.units,316);assert.equal(inv.assigned_ratings,992);assert.equal(inv.variables,14);
 assert.deepEqual(inv.unit_types,{case_source:36,coverage:100,document:33,financial:12,governance:11,observation:124});
});
test('39 original-source records contain bounded excerpts, not conclusions',()=>{
 assert.equal(sources.length,39);assert.equal(new Set(sources.map(s=>s.original_url)).size,39);
 for(const s of sources){assert.match(s.original_url,/^https:\/\//);assert.match(s.reviewed_text_sha256,/^[0-9a-f]{64}$/);assert(s.fragments.reduce((n,f)=>n+f.quote.split(/\s+/).length,0)<=250);assert(!('source_role' in s));}
 assert.equal(sources.reduce((n,s)=>n+s.fragments.length,0),169);
});
test('reviewer forms have no prefilled classifications or narratives',()=>{
 assert.match(python(`import csv,pathlib
p=pathlib.Path('public/validation/reviewer')
rows=list(csv.DictReader((p/'ratings.csv').open()))
assert len(rows)==992
assert all(r['coding_status']=='pending' and not any(r[k] for k in ['reviewer_id','value','rationale','evidence_anchor','source_access']) for r in rows)
notes=list(csv.DictReader((p/'unit-notes.csv').open()))
assert len(notes)==316 and all(not any(v for k,v in r.items() if k!='unit_id') for r in notes)
print('ok')`),/ok/);
});
test('reviewer archive excludes key, baseline, interpretations and old identifiers',()=>{
 assert.match(python(`import zipfile,json,pathlib
p=pathlib.Path('public/validation')
with zipfile.ZipFile(p/'reviewer-pack.zip') as z:
 names=z.namelist()
 assert not any('baseline' in n or 'key.json' in n or 'comparison' in n for n in names)
 for n in names:
  text=z.read(n).decode()
  assert 'impldoc-' not in text and 'obs-rail-' not in text and 'govlink-' not in text
  assert 'github.com/nawaaaaaAaar' not in text
  assert 'change_in_understanding' not in text and 'baseline_stage' not in text
print('ok')`),/ok/);
});
test('masking keys and source references resolve without original-case IDs',()=>{
 assert.match(python(`import csv,json,pathlib
p=pathlib.Path('public/validation/reviewer')
sources=json.loads((p/'sources.json').read_text());ids={s['source_id'] for s in sources};frags={f['fragment_id'] for s in sources for f in s['fragments']}
cases={r['case_id'] for r in csv.DictReader((p/'cases.csv').open())}
units=list(csv.DictReader((p/'units.csv').open()))
assert len({u['unit_id'] for u in units})==316
for u in units:
 assert set(json.loads(u['source_ids']))<=ids and set(json.loads(u['fragment_ids']))<=frags
 assert set(json.loads(u['case_ids']))<=cases
print('ok')`),/ok/);
});
test('manager financial projections and qualitative reference are explicit',()=>{
 assert.equal(json('manager/baseline-projections.json').length,12);
 assert(json('manager/baseline-projections.json').every(p=>/Retrospective/.test(p.provenance)));
 assert.equal(json('manager/qualitative-reference.json').length,124);
});
test('each case has all ten coverage tasks',()=>{
 assert.match(python(`import csv,json,pathlib,collections
p=pathlib.Path('public/validation/reviewer')
u=[r for r in csv.DictReader((p/'units.csv').open()) if r['unit_kind']=='coverage']
counts=collections.Counter(json.loads(r['case_ids'])[0] for r in u)
assert len(counts)==10 and set(counts.values())=={10}
print('ok')`),/ok/);
});
test('shared CAG observations are not duplicated into 136 coding units',()=>{
 assert.equal(inv.unit_types.observation,124);
 assert.match(python(`import csv,json,pathlib
u=list(csv.DictReader(pathlib.Path('public/validation/reviewer/units.csv').open()))
assert sum(len(json.loads(r['case_ids']))>1 for r in u if r['unit_kind']=='observation')==12
print('ok')`),/ok/);
});
test('agreed-item source audit sample is fixed but not falsely completed',()=>{
 assert.match(python(`import csv,pathlib
r=list(csv.DictReader(pathlib.Path('private-validation/manager/control-check-sample.csv').open()))
assert len(r)==33 and len({x['source_id'] for x in r})==33
assert all(x['audit_status']=='pending' and not x['auditor'] for x in r)
print('ok')`),/ok/);
});
test('untouched review template produces zero pairs, not a reliability claim',()=>{
 assert.match(python(`import tempfile,subprocess,json,pathlib
with tempfile.TemporaryDirectory() as t:
 subprocess.run(['python','scripts/compare_coding.py','--reference','private-validation/manager/baseline.csv','--review','public/validation/reviewer/ratings.csv','--schema','public/validation/reviewer/variables.json','--units','public/validation/reviewer/units.csv','--out',t],check=True,capture_output=True)
 s=json.loads(pathlib.Path(t,'agreement.json').read_text())
 assert s['state']=='waiting_for_second_review' and s['paired_ratings']==0
 assert all(m['observed_agreement'] is None and m['kappa'] is None for m in s['metrics'].values())
print('ok')`),/ok/);
});
test('both separate archives match their payload manifests and inventory hashes',()=>{
 for(const [folder,file,key] of [['reviewer','reviewer-pack.zip','reviewer_zip_sha256'],['manager','manager-kit.zip','manager_zip_sha256']]){
  const location=folder==='manager'?new URL('private-validation/',root):base;
  assert.equal(hash(fs.readFileSync(new URL(file,location))),inv[key]);
  const manifest=json(`${folder}/manifest.json`);
  for(const f of manifest.files)assert.equal(hash(fs.readFileSync(new URL(`${folder}/${f.path}`,location))),f.sha256);
 }
 assert.match(python(`import zipfile,json,pathlib,hashlib
p=pathlib.Path('public/validation')
for path in [p/'reviewer-pack.zip',pathlib.Path('private-validation/manager-kit.zip')]:
 with zipfile.ZipFile(path) as z:
  m=json.loads(z.read('manifest.json'))
  assert len(z.namelist())==len(m['files'])+2
  for f in m['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
print('ok')`),/ok/);
});
test('coordinator keys and baseline ZIP stay out of public Git tracking',()=>{
 const out=execFileSync('git',['check-ignore','private-validation/manager/key.json','private-validation/manager-kit.zip'],{cwd:root}).toString();
 assert(out.includes('manager/key.json')&&out.includes('manager-kit.zip'));
 assert(!fs.existsSync(new URL('manager/key.json',base))&&!fs.existsSync(new URL('manager-kit.zip',base)));
});
test('synthetic statistical and adjudication tests pass without fabricating a reviewer',()=>{
 const out=execFileSync('python',['tests/test_review_agreement.py'],{cwd:root,encoding:'utf8',stdio:['ignore','pipe','pipe']});
 assert.equal(out,'');
});
test('repackaging refuses to overwrite an edited reviewer response',()=>{
 assert.match(python(`import pathlib,subprocess
p=pathlib.Path('public/validation/reviewer/ratings.csv');old=p.read_bytes()
try:
 modified=old+b'edited synthetic submission marker\\n';p.write_bytes(modified)
 r=subprocess.run(['python','scripts/build_validation.py'],capture_output=True,text=True)
 assert r.returncode!=0 and 'refusing to overwrite' in r.stderr
 assert p.read_bytes()==modified
finally:p.write_bytes(old)
print('ok')`),/ok/);
});
