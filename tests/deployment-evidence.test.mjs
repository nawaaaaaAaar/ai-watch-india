import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {caseObservations,filterCases} from '../src/deployment-evidence-lib.mjs';
const base=new URL('../public/implementation-evidence/',import.meta.url);
const json=f=>JSON.parse(fs.readFileSync(new URL(f,base)));
const d=json('data.json'),r=JSON.parse(fs.readFileSync(new URL('../public/registry/data.json',import.meta.url))),g=JSON.parse(fs.readFileSync(new URL('../public/governance/data.json',import.meta.url)));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const obs=id=>d.observations.find(o=>o.observation_id===`obs-${id}`);
test('implementation deepens ten existing families without changing population',()=>{
 assert.equal(d.cases.length,10);assert.equal(r.systems.length,144);assert.equal(g.instruments.length,52);
 assert.deepEqual(d.system_keys.map(s=>s.system_id),r.systems.map(s=>s.system_id));
 assert.deepEqual(d.governance_keys.map(i=>i.instrument_id),g.instruments.map(i=>i.instrument_id));
 assert(d.cases.every(c=>r.systems.some(s=>s.system_id===c.system_id)));
});
test('all 528 earlier registry and governance files are byte preserved',()=>{
 const b=json('baseline-layers.json');assert.equal(b.files.length,528);
 for(const f of b.files)assert.equal(hash(fs.readFileSync(new URL(`../${f.path}`,import.meta.url))),f.sha256,f.path);
});
test('twelve linked tables retain unique primary keys and inventory',()=>{
 assert.equal(Object.keys(d.metadata.counts).length,12);assert.equal(d.documents.length,33);assert.equal(d.observations.length,124);
 for(const [t,n] of Object.entries(d.metadata.counts)){assert.equal(d[t].length,n);assert.equal(new Set(d[t].map(x=>Object.values(x)[0])).size,n);}
});
test('all ten dimensions survive per case with explicit unknowns',()=>{
 assert.equal(d.coverage.length,100);assert.equal(d.coverage.filter(v=>!v.observation_ids.length).length,44);
 for(const c of d.cases){const v=d.coverage.filter(v=>v.system_id===c.system_id);assert.equal(v.length,10);assert.equal(new Set(v.map(v=>v.dimension)).size,10);assert(v.every(v=>v.unknown_or_next_record&&/Not evidence/.test(v.absence_interpretation)));}
});
test('scalar and array joins preserve both existing layers',()=>{
 for(const [t,s] of Object.entries(json('schema.json')))for(const row of d[t])for(const [col,[target,key]] of Object.entries(s.foreign_keys))assert(d[target].some(x=>x[key]===row[col]));
 for(const l of d.case_observations)assert(l.registry_assertion_ids.every(id=>r.assertions.some(a=>a.assertion_id===id&&a.system_id===l.system_id)));
 for(const v of d.coverage)assert(v.observation_ids.every(id=>caseObservations(d,v.system_id).some(o=>o.observation_id===id)));
 for(const l of d.governance_links){const old=g.system_links.find(o=>o.system_link_id===l.existing_governance_link_id);assert.equal(old.instrument_id,l.instrument_id);assert.equal(old.system_id,l.system_id);assert.deepEqual(old.instrument_evidence_ids,l.instrument_evidence_ids);assert(l.implementation_observation_ids.every(id=>caseObservations(d,l.system_id).some(o=>o.observation_id===id)));}
});
test('all excerpts retain provenance and bounded quote-audit receipts',()=>{
 const q=json('quote-audit.json');assert.equal(q.length,33);assert(q.every(v=>v.selected_passages_match&&v.selected_words<=250));
 for(const e of d.evidence){assert(e.passage_match);assert(e.locator&&e.quote&&e.verification_mode);assert.equal(e.source_url,d.documents.find(v=>v.document_id===e.document_id).url);}
 for(const doc of d.documents){assert.match(doc.url,/^https:\/\//);assert.match(doc.reviewed_text_sha256,/^[a-f0-9]{64}$/);assert(fs.existsSync(new URL(doc.snapshot,base)));}
});
test('no independent effectiveness, spending or compliance inferred',()=>{
 assert(d.observations.every(o=>!o.independent_outcome_verified));assert(d.cases.every(c=>!c.independent_outcome_verified));
 assert(d.financial_observations.every(f=>!f.actual_spending_verified));assert(d.governance_links.every(l=>!l.compliance_verified));
});
test('source dates, cached recovery and targeted scope remain visible',()=>{
 assert.equal(d.documents.filter(v=>v.is_cached).length,23);
 assert(d.documents.some(v=>v.document_date===null&&v.date_precision==='Not established'));
 assert.equal(d.documents.find(v=>v.label==='rail-spec').document_date,'2024-10-24');
 assert.equal(d.documents.find(v=>v.label==='nhai-tcil').document_date,'2025-07-10');
 assert.match(d.documents.find(v=>v.label==='igms-guidelines').document_kind,/not guidelines/);
 assert.match(d.documents.find(v=>v.label==='nhai-tcil').review_depth,/Targeted/);
});
test('rail false-alarm threshold and field trials are prescribed not outcomes',()=>{
 assert.match(obs('rail-spec-04').statement,/5%.*targets/);assert.equal(obs('rail-spec-04').claim_type,'Requirement / specification');
 assert.match(obs('rail-spec-03').statement,/six months/);assert.match(obs('rail-operation-02').statement,/981.*does not say/);
});
test('VSS named invitation and undated station account remain distinct',()=>{
 assert.match(obs('vss-2025-tender-01').statement,/does not establish.*awarded/);
 assert.match(obs('vss-status-01').statement,/2,077.*does not date/);
 assert.equal(obs('vss-status-01').event_date,null);
});
test('NHAI controls do not imply award or nationwide completion',()=>{
 assert.match(obs('nhai-tcil-04').statement,/before financial opening/);
 assert.match(obs('nhai-tcil-06').statement,/mask number plates and human faces/);
 assert.match(obs('nhai-status-03').statement,/initiated.*not.*completed/);
});
test('court exceptions, monthly reporting and supplier ambiguity remain',()=>{
 assert.match(obs('court-order-03').statement,/record reasons/);assert.match(obs('court-order-04').statement,/monthly/);
 assert.match(obs('court-followup-04').statement,/does not establish whether.*same entity/);
 assert.equal(obs('court-followup-03').event_date,'2026-09');
});
test('CAG shared EOI is not two procurements or contractual obligation',()=>{
 assert.match(obs('cag-eoi-02').statement,/no contractual obligation/);
 assert.match(obs('cag-eoi-05').statement,/final decisions.*designated officers/);
 assert.equal(d.case_observations.filter(l=>l.observation_id==='obs-cag-eoi-02').length,2);
 assert.match(obs('cag-order-01').limitation,/does not establish use of PARAS or PARAKH/);
});
test('Safe Kerala preserves sanction, supplier-account and OCR boundaries',()=>{
 assert.match(obs('safe-order-01').statement,/authorization.*not evidence.*paid/);
 assert.equal(obs('safe-report-02').evidence_strength,"Implementer's historical account");
 assert.match(obs('safe-report-02').statement,/151,22,709,44/);
 assert.match(d.documents.find(v=>v.label==='safe-order').extraction_limit,/font-mangled/);
 assert.match(d.evidence.find(e=>e.observation_id==='obs-safe-order-01').verification_mode,/visual/);
});
test('old UPSC tender is not automatically the own mobile app contract',()=>{
 assert.equal(obs('upsc-tender-04').current_version_match,'Not established');
 assert.match(obs('upsc-status-recovery-02').statement,/technical support.*no commercial supplier/);
 assert.match(obs('upsc-recent-03').statement,/does not state whether/);
});
test('Madukkarai sanction and operator chain are not measured effectiveness',()=>{
 assert.match(obs('tn-launch-02').statement,/sanctioned.*not.*expenditure/);
 assert.match(obs('tn-launch-04').statement,/control room/);
 assert(!caseObservations(d,'sys-madukkarai-elephant').some(o=>/Gudalur/.test(o.statement)));
});
test('IGMS versions and chronology conflict are preserved without causal claims',()=>{
 assert.match(obs('igms-g2g-01').limitation,/conflicts/);
 assert.match(obs('igms-guidelines-02').limitation,/chronology is unresolved/);
 assert.match(obs('igms-aug-04').statement,/under development/);
 assert.match(obs('igms-rfp-03').statement,/manually closes/);
 assert.match(obs('igms-prebid-05').statement,/LLM training/);
});
test('selection and research logs are reproducible and do not claim census',()=>{
 assert.equal(d.selection_decisions.length,12);assert.equal(d.selection_decisions.filter(s=>s.disposition==='Deferred after screening').length,2);
 const log=json('search-log.json');assert.equal(log.length,96);assert.equal(log.reduce((n,r)=>n+r.hits,0),575);
 assert.equal(json('retrieval-log.json').length,66);assert.match(json('review-decisions.json').retrieval_log_limit,/overwritten/);
});
test('search/dimension/strength and reset operate on case-linked evidence',()=>{
 assert.equal(filterCases(d).length,10);assert.equal(filterCases(d,{query:'Intellve'}).length,1);
 assert.equal(filterCases(d,{query:'nosuchzzzz'}).length,0);
 assert.equal(filterCases(d,{dimension:'Contracts and awards'}).length,0);
 assert.equal(filterCases(d,{strength:"Implementer's historical account"}).length,1);
 assert.equal(filterCases(d,{query:'Intellve',strength:'Formal prescribed requirement'}).length,1);
 assert.equal(filterCases(d,{query:'Intellve',strength:"Implementer's historical account"}).length,0);
});
test('SQLite integrity, scalar foreign keys and runnable queries pass',()=>{
 const out=execFileSync('python',['-c',`import sqlite3,pathlib
c=sqlite3.connect('public/implementation-evidence/dataset.sqlite')
assert c.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
assert not c.execute('PRAGMA foreign_key_check').fetchall()
assert c.execute('select count(*) from observations').fetchone()[0]==124
for q in pathlib.Path('public/implementation-evidence/queries.sql').read_text().split(';'):
 if q.strip(): c.execute(q).fetchall()
print('ok')`],{cwd:new URL('../',import.meta.url)}).toString();assert.match(out,/ok/);
});
test('manifest and checksummed archive retain payload bytes',()=>{
 const m=json('manifest.json');
 for(const f of m.files){const b=fs.readFileSync(new URL(f.path,base));assert.equal(b.length,f.bytes);assert.equal(hash(b),f.sha256);}
 assert.equal(fs.readFileSync(new URL('manifest.sha256',base),'utf8').split(' ')[0],hash(fs.readFileSync(new URL('manifest.json',base))));
 const out=execFileSync('python',['-c',`import zipfile,pathlib,json,hashlib
p=pathlib.Path('public/implementation-evidence')
with zipfile.ZipFile(p/'complete-implementation-evidence.zip') as z:
 m=json.loads(z.read('manifest.json'))
 for f in m['files']:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
 assert len(z.namelist())==len(m['files'])+2
print('ok')`],{cwd:new URL('../',import.meta.url)}).toString();assert.match(out,/ok/);
});
