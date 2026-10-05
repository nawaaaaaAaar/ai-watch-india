import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
const root=new URL('../public/registry/',import.meta.url);
const d=JSON.parse(fs.readFileSync(new URL('data.json',root)));
const phase=JSON.parse(fs.readFileSync(new URL('../research/registry-phase3.json',import.meta.url)));
const baseline=JSON.parse(fs.readFileSync(new URL('BASELINE_1_1_0.json',root)));
const a=(sid,field)=>d.assertions.find(a=>a.system_id===sid&&a.field===field);
const canonicalValue=v=>Array.isArray(v)?v.map(canonicalValue):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,canonicalValue(v[k])])):v;
test('current release retains exactly 36 named earlier broadening families',()=>{
 assert.equal(d.metadata.version,'1.3.0');assert.equal(d.systems.length,144);assert.equal(d.assertions.length,1728);
 assert.equal(d.systems.filter(s=>s.research_round==='1.0.0').length,18);
 assert.equal(d.systems.filter(s=>s.research_round==='1.1.0').length,18);
 assert.equal(d.systems.filter(s=>s.research_round==='1.2.0').length,36);
 assert.equal(phase.profiles.length,36);
});
test('every original row value survives rather than only selected baseline examples',()=>{
 for(const [t,records] of Object.entries(baseline.tables))for(const r of records){
  const row=d[t].find(x=>x[r.primary_key]===r.id);assert(row,`${t}:${r.id}`);
  const projected=Object.fromEntries(r.keys.map(k=>[k,row[k]]));
  // Preserve nested receipt keys while applying Python's recursive canonical sorting.
  const canonical=JSON.stringify(canonicalValue(projected));
  assert.equal(crypto.createHash('sha256').update(canonical).digest('hex'),r.sha256,`${t}:${r.id}`);
 }
});
test('all thirty-six additions have deployment observations with report-date qualifiers',()=>{
 const ids=new Set(phase.profiles.map(p=>p.system_id));
 const rows=d.deployments.filter(r=>ids.has(r.system_id));assert.equal(rows.length,36);
 for(const r of rows)assert.match(r.date_precision,/not actual go-live/);
});
test('all forty-nine new sources have positive original-text selection checks and budgets',()=>{
 const rows=JSON.parse(fs.readFileSync(new URL('BROADENING_QUOTE_AUDIT.json',root)));
 assert.equal(rows.length,49);assert.equal(d.sources.filter(s=>s.source_id.startsWith('ext-')).length,49);
 for(const r of rows){assert(r.all_selected_passages_match);assert(r.selected_words<=250);assert.match(r.fetched_text_sha256,/^[a-f0-9]{64}$/);}
});
test('broadening research keeps 153 queries, 693 leads and all hundred retrieval receipts',()=>{
 const q=JSON.parse(fs.readFileSync(new URL('BROADENING_SEARCH.json',root)));
 const r=JSON.parse(fs.readFileSync(new URL('BROADENING_RETRIEVAL.json',root)));
 assert.equal(q.queries.length,153);assert.equal(q.hits.length,693);assert.equal(q.errors.length,0);
 assert.equal(r.length,100);assert.equal(r.filter(x=>x.status==='Failed').length,3);
 assert(r.every(x=>!x.content&&!x.snippet));
});
test('YAKSH legacy apps and regional iRASTE deployments do not pad the count',()=>{
 assert.equal(d.systems.filter(s=>s.research_round==='1.2.0'&&/YAKSH|Trinetra/i.test(s.name)).length,1);
 assert.equal(d.systems.filter(s=>/iRASTE/i.test(s.name)).length,1);
 assert(d.candidate_decisions.some(c=>c.name==='Trinetra standalone extra row'));
 assert(d.candidate_decisions.some(c=>c.name==='iRASTE Nagpur standalone extra row'));
});
test('generic DAKSH and KSMART umbrella digital platforms remain deferred',()=>{
 assert(!d.systems.some(s=>/DAKSH|K-SMART/i.test(s.name)));
 assert(d.candidate_decisions.some(c=>c.name==='RBI DAKSH'));
 assert(d.candidate_decisions.some(c=>c.name==='K-SMART generic platform'));
});
test('Safe Kerala suspension limits refer to processing and not every camera being off',()=>{
 assert.match(d.systems.find(s=>s.system_id==='sys-safe-kerala').stage,/suspended/);
 assert.match(a('sys-safe-kerala','Current-status limits').value,/neither camera hardware shutdown everywhere/);
});
test('Delhi approval remains an estimated cost and a prospective competitive award',()=>{
 const p=d.procurements.find(p=>p.system_id==='sys-delhi-itms');
 assert.equal(p.amount_inr,17895200000);assert.equal(p.supplier_institution_id,null);
 assert.match(p.amount_type,/not spending/);
 assert.match(a('sys-delhi-itms','Procurement & supplier').value,/Future competitively selected/);
});
test('reported SANJAY developed cost is not independently reconciled spending',()=>{
 const p=d.procurements.find(p=>p.system_id==='sys-sanjay');assert.equal(p.amount_inr,24020000000);
 assert.match(p.amount_type,/not reconciled/);
 assert.equal(d.systems.find(s=>s.system_id==='sys-sanjay').ai_class,'Qualified algorithmic / biometric context');
});
test('FRI analytical risk categories remain qualified and financial claims self-reported',()=>{
 assert.equal(d.systems.find(s=>s.system_id==='sys-fri').ai_class,'Qualified algorithmic / biometric context');
 const m=d.metrics.find(m=>m.system_id==='sys-fri');assert.equal(m.value,5043.73);
 assert.match(m.metric_kind,/self-report/);assert.match(m.measurement_scope,/not independently verified/);
});
test('iOncology historical benchmark and clinical validation are distinct claims',()=>{
 assert.match(a('sys-ioncology','Evaluation & error rates').value,/over 75%/);
 assert.match(a('sys-ioncology','Evaluation & error rates').value,/no established peer-reviewed clinical validation/);
 assert.equal(d.evaluations.find(e=>e.system_id==='sys-ioncology').sample_n,1500);
});
test('iRASTE observational outcome is not a randomised AI-only effect',()=>{
 const e=d.evaluations.find(e=>e.system_id==='sys-iraste');
 assert.equal(e.sample_n,200);assert.match(e.evaluation_type,/observational/);
 assert.match(e.result_summary,/not causally isolated/);
 assert.equal(d.metrics.find(m=>m.system_id==='sys-iraste').value,40);
});
test('Saagu Baagu reported yield gains stay bundled multi-intervention outcomes',()=>{
 const m=d.metrics.find(m=>m.system_id==='sys-saagu-baagu');
 assert.equal(m.value,21);assert.equal(m.metric_kind,'Multi-intervention outcome self-report');
 assert.match(m.measurement_scope,/not isolated/);
});
test('helpline quality approval is a tender requirement not verified enforcement',()=>{
 const c=d.controls.find(c=>c.system_id==='sys-ksh');
 assert.match(c.description,/not verified execution/);
 assert.match(a('sys-ksh','Procurement & supplier').value,/not an awarded/);
 assert(d.issues.some(i=>i.system_id==='sys-ksh'&&i.description.includes('artificial insemination')));
});
test('Raj Silicosis workflow rhetoric is not a fabricated diagnostic-accuracy metric',()=>{
 assert(!d.metrics.some(m=>m.system_id==='sys-raj-silicosis'));
 assert.match(a('sys-raj-silicosis','Evaluation & error rates').value,/not a diagnostic benchmark/);
});
test('official NUWR developer is not misassigned from an adjacent catalogue project',()=>{
 const role=d.system_institutions.find(r=>r.system_id==='sys-nuwr-analysis'&&d.institutions.find(i=>i.institution_id===r.institution_id)?.name==='Bharat Forge Limited');
 assert(role);
 assert(!d.system_institutions.some(r=>r.system_id==='sys-nuwr-analysis'&&d.institutions.find(i=>i.institution_id===r.institution_id)?.name==='Bharat Electronics Limited'));
});
test('latest study covers every addition and source URL without removing prior research',()=>{
 const text=fs.readFileSync(new URL('BROADENING_STUDY.md',root),'utf8');
 for(const p of phase.profiles)assert(text.includes('### '+p.name));
 for(const s of phase.sources)assert(text.includes(s.url),s.source_id);
 assert(fs.existsSync(new URL('INSTITUTION_STUDY.md',root)));assert(fs.existsSync(new URL('RESEARCH_NOTE.md',root)));
});
