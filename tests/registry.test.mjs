import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {filterSystems,registryCsv,recordEvidence} from '../src/registry-lib.mjs';
const root=new URL('../public/registry/',import.meta.url);
const d=JSON.parse(fs.readFileSync(new URL('data.json',root)));
const pk=t=>Object.keys(d[t][0])[0];
const ids=t=>new Set(d[t].map(r=>r[pk(t)]));
test('registry is separate: seventy-two named systems with all twelve assertion slots',()=>{
 assert.equal(d.systems.length,72);assert.equal(d.assertions.length,864);
 for(const s of d.systems)assert.deepEqual(d.assertions.filter(a=>a.system_id===s.system_id).map(a=>a.field),d.metadata.field_order);
 assert.equal(d.systems.filter(s=>s.legacy_id).length,6);
});
test('all twenty-one table keys are unique',()=>{
 assert.equal(Object.keys(d.metadata.counts).length,21);
 for(const t of Object.keys(d.metadata.counts)){assert.equal(ids(t).size,d[t].length);assert.equal(d.metadata.counts[t],d[t].length);}
});
test('all system, institution and source references are valid',()=>{
 for(const t of Object.keys(d.metadata.counts))for(const r of d[t]){
  if(r.system_id)assert(ids('systems').has(r.system_id));
  if(r.target_system_id)assert(ids('systems').has(r.target_system_id));
  if(r.source_id)assert(ids('sources').has(r.source_id));
  if(r.evidence_id)assert(ids('evidence').has(r.evidence_id));
  for(const k of ['institution_id','owner_institution_id','supplier_institution_id'])if(r[k])assert(ids('institutions').has(r[k]));
 }
});
test('generic provenance relationships and assertion evidence have no orphan',()=>{
 for(const l of d.evidence_links){assert(ids(l.record_type).has(l.record_id));assert(ids('evidence').has(l.evidence_id));}
 for(const a of d.assertions)if(a.evidence_status!=='Not verified')assert(recordEvidence(d,'assertions',a.assertion_id).length>0);
});
test('no invented source or go-live dates',()=>{
 for(const s of d.sources)if(s.published_date)assert.match(s.published_date,/^\d{4}-\d{2}-\d{2}$/);
 assert.equal(d.sources.find(s=>s.source_id==='reg-vistaar-portal').published_date,null);
 assert.equal(d.sources.find(s=>s.source_id==='reg-cag-bhashini').published_date,'2026-09-30');
 assert.equal(d.sources.find(s=>s.source_id==='reg-insight-contract').published_date,'2016-07-19');
 assert.equal(d.systems.find(s=>s.system_id==='sys-insight').latest_record_date,'2016-07-19');
 const planned=d.deployments.find(r=>r.system_id==='sys-insight'&&r.event_date==='2017-05');
 assert.equal(planned.stage,'Expected launch');assert.match(planned.description,/not treated as achieved/);
});
test('study specificity survives alongside headline accuracy and sample limits',()=>{
 const ms=d.metrics.filter(m=>m.system_id==='sys-epaarvai');
 assert.equal(ms.find(m=>m.metric_name==='Specificity').value,25);
 assert.equal(ms.find(m=>m.metric_name==='Accuracy').value,88);
 assert.equal(ms.length,5);
 assert.equal(d.evaluations.find(e=>e.system_id==='sys-epaarvai').sample_n,1407);
 assert.match(d.evaluations.find(e=>e.system_id==='sys-epaarvai').current_version_match,/not verified/);
});
test('normative IDS alarm threshold is not observed model accuracy',()=>{
 const m=d.metrics.find(m=>m.metric_name==='Maximum false-alarm share');
 assert.equal(m.metric_kind,'Specification threshold');assert.match(m.denominator,/generated alarms/);
 assert.match(m.value_qualifier,/not observation/);
 const outcome=d.metrics.find(m=>m.metric_name==='Reported elephants saved');assert.match(outcome.measurement_scope,/not causal IDS-only/);
});
test('allocations, historical announced contracts and reported regional awards stay distinct',()=>{
 assert.equal(d.procurements.length,5);
 assert.equal(d.procurements.find(p=>p.system_id==='sys-bharat-vistaar').amount_inr,1500000000);
 assert.match(d.procurements.find(p=>p.system_id==='sys-bharat-vistaar').amount_type,/not spending/);
 assert.equal(d.procurements.find(p=>p.system_id==='sys-insight').amount_inr,null);
 assert.equal(d.procurements.find(p=>p.system_id==='sys-rail-ids').amount_inr,189900000);
});
test('numeric usage lower bounds are explicitly qualified',()=>{
 const rows=d.metrics.filter(m=>m.metric_kind==='Usage self-report');
 assert.equal(rows.length,4);for(const m of rows)assert.equal(m.value_qualifier,'More than stated lower bound');
});
test('AI subset and qualified contexts are filterable without making biometrics a model claim',()=>{
 assert.equal(filterSystems(d,{ai:'Explicit source attribution'}).length,61);
 assert.equal(filterSystems(d,{ai:'Qualified algorithmic / biometric context'}).length,10);
 assert.equal(filterSystems(d,{ai:'AI evaluation infrastructure'}).length,1);
 assert.match(d.systems.find(s=>s.system_id==='sys-insight').ai_basis,/not verified/);
});
test('search supports institution, narrative evidence, case insensitive and AND terms',()=>{
 assert(filterSystems(d,{query:'SPECIFICITY 25%'}).some(s=>s.system_id==='sys-epaarvai'));
 assert.equal(filterSystems(d,{query:'UNFINDABLEZZZ'}).length,0);
 assert.equal(filterSystems(d,{query:'Bharat VISTAAR'}).length,1);
 assert.equal(filterSystems(d,{query:'CoRover'}).length,1);
});
test('filters and source-date sorting are reproducible',()=>{
 const rows=filterSystems(d,{sort:'date'});
 assert.equal(rows.at(-1).latest_record_date,null);
 assert.equal(filterSystems(d,{sector:'Tax administration'}).length,3);
 assert.equal(filterSystems(d,{sector:'Tax administration',ai:'Explicit source attribution'}).length,2);
});
test('filtered CSV is typed-context export, escapes formulas and retains null dates',()=>{
 const text=registryCsv(d,filterSystems(d,{sector:'Tax administration'}));
 assert.equal(text.trim().split(/\r?\n/).length,4);assert.match(text,/dossiers\/sys-insight.md/);
 assert(registryCsv(d,[{...d.systems[0],name:'=CMD()'}]).includes("'=CMD()"));
});
test('all snapshots have matching SHA-256 and original source URLs',()=>{
 for(const s of d.sources){const b=fs.readFileSync(new URL(s.snapshot,root));assert.equal(crypto.createHash('sha256').update(b).digest('hex'),s.snapshot_sha256);assert(b.toString().includes(s.url));}
});
test('all thirty-six dossiers include every field and supporting source URLs',()=>{
 for(const s of d.systems){const text=fs.readFileSync(new URL(`dossiers/${s.system_id}.md`,root),'utf8');for(const f of d.metadata.field_order)assert(text.includes('## '+f));assert.match(text,/https:\/\//);}
});
test('selection and rejected foreign validation are transparent',()=>{
 assert(d.candidate_decisions.some(c=>c.name==='Nigeria qXR clinical study'&&c.decision.includes('Excluded')));
 assert(!d.evidence.some(e=>e.source_id==='reg-qxr-study'));
 assert(d.candidate_decisions.some(c=>c.name==='DCI Social Protection AI Hub Kisan e-Mitra entry'));
});
test('archive, SQLite and runnable queries reproduce with valid integrity',()=>{
 const code=`import sqlite3,zipfile,json,hashlib,pathlib
p=pathlib.Path('public/registry')
c=sqlite3.connect(p/'dataset.sqlite')
assert c.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
assert not c.execute('PRAGMA foreign_key_check').fetchall()
assert c.execute('SELECT COUNT(*) FROM systems').fetchone()[0]==72
c.executescript((p/'queries.sql').read_text())
with zipfile.ZipFile(p/'complete-registry.zip') as z:
 assert z.testzip() is None
 m=json.loads(z.read('manifest.json'))
 assert len(z.namelist())==len(m['files'])+2
 for f in m['files']:
  assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
`;
 execFileSync('python',['-c',code],{cwd:new URL('../',import.meta.url)});
});
test('new source excerpt selections are bounded and not whole papers',()=>{
 for(const s of d.sources.filter(s=>/^(reg|frame|ext)-/.test(s.source_id))){const qs=d.evidence.filter(e=>e.source_id===s.source_id).map(e=>e.quote);assert(qs.join(' ').split(/\s+/).length<=250);}
});
test('search and retrieval logs preserve failures without copying full article text',()=>{
 const search=JSON.parse(fs.readFileSync(new URL('search-log.json',root)));
 assert.equal(search.length,62);assert.equal(search.flatMap(s=>s.hits).length,312);
 const logs=JSON.parse(fs.readFileSync(new URL('retrieval-log.json',root)));
 assert(logs.some(s=>s.retrieval_status.includes('failed')||s.retrieval_status==='Failed'));
 assert(logs.every(s=>!s.content&&!s.snippet));
});
test('primary data route preserves supporting policy routes and naming',()=>{
 const app=fs.readFileSync(new URL('../src/main.tsx',import.meta.url),'utf8');
 assert(app.includes('<Route path="/"><Registry/></Route>'));
 assert(app.includes('path="/desk"'));assert(app.includes('path="/compare/:id"'));
 assert(app.includes('INDIA EVIDENCE DESK'));assert(app.includes('Policy notebook'));
 assert(app.includes("response.headers.get('content-type')?.includes('text/html')"));
});
test('fixed six-institution frame is complete and ownership is not inferred',()=>{
 assert.equal(d.institution_coverage.length,6);assert.equal(d.coverage_systems.length,26);
 for(const f of d.institution_coverage){assert.equal(f.base_queries,4);assert.match(f.coverage_status,/not exhaustive/);}
 assert.equal(filterSystems(d,{frame:'frame-home'}).length,4);
 assert.equal(filterSystems(d,{frame:'frame-health'}).length,6);
 assert.equal(filterSystems(d,{frame:'Outside frame'}).length,46);
});
test('same structural source audit covers every baseline source and field',()=>{
 assert.equal(d.source_rechecks.length,50);assert.equal(d.assertion_rechecks.length,216);
 for(const r of d.source_rechecks){assert(ids('sources').has(r.source_id));assert.match(r.note,/not independent/);}
 for(const r of d.assertion_rechecks)assert(ids('assertions').has(r.assertion_id));
 assert.equal(d.source_rechecks.reduce((n,r)=>n+r.matched_excerpts,0),68);
 assert.equal(d.source_rechecks.reduce((n,r)=>n+r.total_excerpts,0),125);
});
test('cached retrieval does not masquerade as fresh re-verification',()=>{
 const failed=d.source_rechecks.filter(r=>r.status.startsWith('Retrieval failed'));
 assert.equal(failed.length,20);
 for(const r of failed){assert.equal(r.cached_retry_matches,r.total_excerpts);assert.match(r.cached_retry_basis,/not fresh/);}
});
test('channel-specific July evidence refines Bharat-VISTAAR without erasing history',()=>{
 const rows=d.issues.filter(i=>i.system_id==='sys-bharat-vistaar');
 assert(rows.some(i=>i.description.includes('ten-language')));
 assert(rows.some(i=>i.description.includes('22+')));
 assert.equal(d.systems.find(s=>s.system_id==='sys-bharat-vistaar').latest_record_date,'2026-07-24');
});
test('new clinical claims stay self-reports and range bounds are machine-readable',()=>{
 const m=d.metrics.find(m=>m.system_id==='sys-catb');
 assert.equal(m.value,12);assert.equal(m.value_upper,16);
 assert.match(m.metric_kind,/protocol unavailable/);assert.match(m.measurement_scope,/Not sensitivity/);
 assert.equal(d.systems.find(s=>s.system_id==='sys-bodh').system_kind,'AI evaluation infrastructure');
});
test('CCTNS version conflict and CROPIC declaration tension are preserved',()=>{
 assert(d.assertions.some(a=>a.system_id==='sys-cctns2'&&a.evidence_status==='Conflicting sources'));
 assert(d.issues.some(i=>i.system_id==='sys-cropic'&&i.description.includes('no-data-collected')));
});
test('frame methodology records all 24 institutional and twelve follow-up queries',()=>{
 const q=JSON.parse(fs.readFileSync(new URL('INSTITUTION_SEARCH.json',root)));
 assert.equal(q.length,36);assert.equal(q.flatMap(x=>x.hits).length,228);
 for(const f of d.institution_coverage)assert.equal(q.filter(x=>x.frame_id===f.frame_id).length,4);
});
test('courses, EOI, unrelated modules and policy are not inflated into live AI units',()=>{
 assert(d.candidate_decisions.some(c=>c.name==='SAHI'&&c.decision==='Context / deferred'));
 assert(d.candidate_decisions.some(c=>c.name==='AI-enabled National Learning Operating System'&&c.reason.includes('not an awarded')));
 assert(!d.systems.some(s=>s.name==='SWAYAM'||s.name==='SAHI'));
});
