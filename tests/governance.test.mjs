import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {filterGovernance} from '../src/governance-lib.mjs';
const base=new URL('../public/governance/',import.meta.url);
const json=f=>JSON.parse(fs.readFileSync(new URL(f,base)));
const d=json('data.json'), r=JSON.parse(fs.readFileSync(new URL('../public/registry/data.json',import.meta.url)));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const instrument=id=>d.instruments.find(i=>i.instrument_id===`gov-${id}`);
test('governance has 52 versions in eleven tables, not extra systems',()=>{
 assert.equal(d.instruments.length,52);assert.equal(Object.keys(d.metadata.counts).length,11);assert.equal(r.systems.length,144);assert.equal(d.system_keys.length,144);
 assert.deepEqual(d.system_keys.map(s=>s.system_id),r.systems.map(s=>s.system_id));
 for(const [t,n] of Object.entries(d.metadata.counts)){assert.equal(d[t].length,n);assert.equal(new Set(d[t].map(x=>Object.values(x)[0])).size,n);}
});
test('all 389 earlier registry payloads are byte preserved',()=>{
 const b=json('baseline-registry.json');assert.equal(b.files.length,389);
 for(const f of b.files)assert.equal(hash(fs.readFileSync(new URL(`../public/registry/${f.path}`,import.meta.url))),f.sha256,f.path);
});
test('every instrument retains five dimension slots and no implemented-control claim',()=>{
 assert.equal(d.provisions.length,260);
 for(const i of d.instruments)assert.deepEqual(d.provisions.filter(p=>p.instrument_id===i.instrument_id).map(p=>p.dimension).sort(),['Oversight','Evaluation','Procurement','Redress','Accountability and data'].sort());
 assert(d.provisions.every(p=>p.implementation_verified===false));assert(d.instruments.every(i=>/Not independently verified/.test(i.implementation_status)));
});
test('scalar foreign keys are valid',()=>{
 for(const [t,s] of Object.entries(json('schema.json')))for(const row of d[t])for(const [col,[target,key]] of Object.entries(s.foreign_keys))if(row[col]!==null)assert(d[target].some(x=>x[key]===row[col]),`${t}.${col}`);
});
test('95 typed links preserve both provenance halves',()=>{
 assert.equal(d.system_links.length,95);assert.equal(new Set(d.system_links.map(l=>l.system_id)).size,54);
 for(const l of d.system_links){assert(l.link_type&&l.rationale&&l.applicability_determination);
  assert(l.instrument_evidence_ids.length&&l.system_assertion_ids.length&&l.system_source_ids.length);
  for(const id of l.instrument_evidence_ids)assert(d.evidence.some(e=>e.evidence_id===id&&e.instrument_id===l.instrument_id));
  for(const id of l.system_assertion_ids)assert(r.assertions.some(a=>a.assertion_id===id&&a.system_id===l.system_id));
  assert.deepEqual([...new Set(l.system_source_urls)].sort(),r.sources.filter(s=>l.system_source_ids.includes(s.source_id)).map(s=>s.url).sort());
 }
});
test('every source is official primary provenance with a bounded snapshot',()=>{
 assert.equal(d.sources.length,56);
 for(const s of d.sources){assert.match(s.source_type,/Primary official/);assert.match(s.url,/^https:\/\//);assert.match(s.reviewed_text_sha256,/^[a-f0-9]{64}$/);assert(fs.existsSync(new URL(s.snapshot,base)));}
 for(const i of d.instruments)assert.equal(i.primary_source_url,d.sources.find(s=>s.source_id===i.primary_source_id).url);
});
test('289 excerpts have passed membership and per-URL quote budget checks',()=>{
 assert.equal(d.evidence.length,289);const audit=json('quote-audit.json');
 assert.equal(audit.length,56);assert(audit.every(a=>a.selected_passages_match&&a.selected_words<=250));
 for(const e of d.evidence)assert(d.sources.some(s=>s.source_id===e.source_id));
});
test('all 37 jurisdictions are retained, including zero-inclusion unknowns',()=>{
 assert.equal(d.jurisdiction_coverage.length,37);assert.equal(new Set(d.jurisdiction_coverage.map(c=>c.jurisdiction)).size,37);
 for(const c of d.jurisdiction_coverage){assert(c.queries.length>=2);assert(c.coverage_limit.length>50);}
 assert(d.jurisdiction_coverage.filter(c=>!c.included_instrument_ids.length).every(c=>/not.*absence|not an official inventory/i.test(c.coverage_limit)));
 assert.equal(new Set(d.instruments.filter(i=>i.jurisdiction!=='Central').map(i=>i.jurisdiction)).size,14);
});
test('four outline-only records do not become full-text review',()=>{
 const rows=d.instruments.filter(i=>i.review_depth==='Official outline / announcement only');assert.equal(rows.length,4);
 assert.deepEqual(rows.map(i=>i.instrument_id).sort(),['gov-icmr-ai','gov-ndgf-draft','gov-tpec-constitution','gov-uttarakhand-mission'].sort());
});
test('eight drafts inherit non-operative proposal force',()=>{
 const drafts=d.instruments.filter(i=>i.document_status==='Draft / consultation');assert.equal(drafts.length,8);
 for(const i of drafts){assert.match(i.legal_effect,/Draft proposal/);assert.match(i.operative_status,/Not operative/);}
});
test('Sikkim remains draft while Maharashtra has a covering adoption resolution',()=>{
 assert.equal(instrument('sikkim-draft').document_status,'Draft / consultation');assert.equal(instrument('sikkim-draft').instrument_date,'2026-03-13');
 assert.equal(instrument('maharashtra-ai').document_status,'Adopted / formally constituted');assert.match(instrument('maharashtra-ai').current_status_limit,/draft label/);
});
test('DPDP staged commencement is not flattened into current duties',()=>{
 for(const id of ['dpdp-act','dpdp-rules','dpdp-correction','dpdp-commencement'])assert.match(instrument(id).operative_status,/Staged commencement/);
 assert.match(instrument('dpdp-rules').commencement_text,/18 months|eighteen months/i);
});
test('synthetic media effective date and corrigendum remain separate',()=>{
 assert.match(instrument('sgi-amendment').commencement_text,/20 February 2026/);
 assert.equal(instrument('sgi-correction').instrument_date,'2026-02-26');
 assert.equal(instrument('sgi-amendment').instrument_family,instrument('sgi-correction').instrument_family);
});
test('source text dates supersede filename/upload metadata',()=>{
 assert.equal(instrument('cert-aibom').instrument_date,'2025-07-09');assert.equal(instrument('sebi-cyber-advisory').instrument_date,'2026-05-05');
 assert.equal(instrument('odisha-ai').instrument_date,'2025-06-18');assert.match(instrument('aadhaar-regulations').commencement_text,/15 December 2025/);
 assert.equal(instrument('rbi-model-risk-draft').instrument_date,'2026-06');assert.equal(instrument('national-strategy').instrument_date,null);
});
test('elapsed Gujarat mandate is historical with renewal unresolved',()=>{
 assert.equal(instrument('gujarat-taskforce').document_status,'Historical mandate / renewal unverified');assert.match(instrument('gujarat-taskforce').legal_effect,/One-year/);
});
test('SEBI intermediary instruments are not attached to regulator-owned tools',()=>{
 for(const l of d.system_links.filter(l=>['gov-sebi-responsibility','gov-sebi-cyber-advisory','gov-sebi-reporting','gov-sebi-funds'].includes(l.instrument_id)))assert(!['sys-seva','sys-sudarsan','sys-infomerge','sys-raidar'].includes(l.system_id));
});
test('court and CAG named links retain direction versus EOI distinctions',()=>{
 const court=d.system_links.find(l=>l.instrument_id==='gov-ap-court-order');assert.equal(court.system_id,'sys-adalat-ai');assert.match(court.link_type,/Explicit|Named/);
 const cag=d.system_links.filter(l=>l.instrument_id==='gov-cag-ai-eoi');assert.equal(cag.length,2);assert(cag.every(l=>/not supplier awards/.test(l.rationale)));
 assert.match(instrument('cag-ai-eoi').document_status,/award unverified/);
});
test('Rajasthan uses scanned full text and explicit AIBOM relationship',()=>{
 const i=instrument('rajasthan-ai');assert.match(i.primary_source_url,/AI%20ML%20POLICY/);assert.match(i.current_status_limit,/OCR/);
 assert(d.instrument_relationships.some(l=>l.instrument_id===i.instrument_id&&l.related_instrument_id==='gov-cert-aibom'));
});
test('contextual grievance and evaluation targets are not concrete controls',()=>{
 const tel=d.provisions.find(p=>p.instrument_id==='gov-telangana-strategy'&&p.dimension==='Redress');assert.notEqual(tel.presence,'Textual provision');
 const ker=d.provisions.find(p=>p.instrument_id==='gov-kerala-it'&&p.dimension==='Evaluation');assert.notEqual(ker.presence,'Textual provision');
 const meg=d.provisions.find(p=>p.instrument_id==='gov-meghalaya-it'&&p.dimension==='Redress');assert.match(meg.summary,/policy|incentive/i);
});
test('search, combined filters and empty results are deterministic',()=>{
 assert.equal(filterGovernance(d).length,52);assert.equal(filterGovernance(d,{jurisdiction:'Central'}).length,37);
 assert.equal(filterGovernance(d,{jurisdiction:'Tamil Nadu'}).length,2);assert.equal(filterGovernance(d,{status:'Draft / consultation'}).length,8);
 assert(filterGovernance(d,{query:'AIBOM'}).some(i=>i.instrument_id==='gov-cert-aibom'));
 assert.equal(filterGovernance(d,{query:'NOTFOUNDQZX'}).length,0);
 assert.equal(filterGovernance(d,{jurisdiction:'Goa',status:'Draft / consultation',type:'Draft state AI policy'}).length,1);
});
test('complete query and retrieval logs disclose attempts and cached recovery',()=>{
 const searches=json('search-log.json');assert.equal(searches.length,157);assert.equal(searches.reduce((s,r)=>s+r.hits,0),948);
 const retrieval=json('retrieval-log.json');assert.equal(retrieval.length,136);assert(retrieval.some(r=>r.error));assert(retrieval.some(r=>r.is_cached));
 assert.equal(d.candidate_decisions.length,13);
});
test('manifest validates every payload and 52 dossiers',()=>{
 const m=json('manifest.json');for(const f of m.files){const b=fs.readFileSync(new URL(f.path,base));assert.equal(b.length,f.bytes);assert.equal(hash(b),f.sha256,f.path);}
 assert.equal(m.files.filter(f=>f.path.startsWith('dossiers/')).length,52);
 assert.equal(json('analysis.json').instrument_families,44);assert.equal(json('analysis.json').linked_instruments,26);
});
test('SQLite integrity, declared FKs, queries and JSON values agree',()=>{
 const result=execFileSync('python',['-c',`import sqlite3,json,pathlib
p=pathlib.Path('public/governance');c=sqlite3.connect(p/'dataset.sqlite');d=json.loads((p/'data.json').read_text())
assert c.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
assert not c.execute('PRAGMA foreign_key_check').fetchall()
for t,n in d['metadata']['counts'].items():assert c.execute('SELECT COUNT(*) FROM '+t).fetchone()[0]==n
statement=''
for line in (p/'queries.sql').read_text().splitlines(True):
 statement+=line
 if sqlite3.complete_statement(statement):
  c.execute(statement).fetchall()
  statement=''
print('ok')`],{cwd:new URL('..',import.meta.url)}).toString();assert.match(result,/ok/);
});
test('ZIP entries exactly match the payload plus manifests',()=>{
 const out=execFileSync('python',['-c',`import pathlib,json,zipfile,hashlib
p=pathlib.Path('public/governance');m=json.loads((p/'manifest.json').read_text())
with zipfile.ZipFile(p/'complete-governance.zip') as z:
 assert z.testzip() is None
 assert set(z.namelist())=={r['path'] for r in m['files']}|{'manifest.json','manifest.sha256'}
 for r in m['files']:assert hashlib.sha256(z.read(r['path'])).hexdigest()==r['sha256']
print('ok')`],{cwd:new URL('..',import.meta.url)}).toString();assert.match(out,/ok/);
});
