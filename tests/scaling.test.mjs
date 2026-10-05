import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {filterSystems,recordEvidence,registryCsv} from '../src/registry-lib.mjs';
const root=new URL('../public/registry/',import.meta.url);
const d=JSON.parse(fs.readFileSync(new URL('data.json',root)));
const phase=JSON.parse(fs.readFileSync(new URL('../research/registry-phase4.json',import.meta.url)));
const a=(sid,f)=>d.assertions.find(a=>a.system_id===sid&&a.field===f);
const canonical=v=>Array.isArray(v)?v.map(canonical):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,canonical(v[k])])):v;
test('second doubling contains exactly 72 additions and four preserved cohorts',()=>{
 assert.equal(d.metadata.version,'1.3.0');assert.equal(d.systems.length,144);assert.equal(d.assertions.length,1728);
 assert.equal(phase.profiles.length,72);
 for(const [cohort,n] of [['1.0.0',18],['1.1.0',18],['1.2.0',36],['1.3.0',72]])assert.equal(filterSystems(d,{cohort}).length,n);
});
test('all row values in every previous table survive full canonical hash comparison',()=>{
 const baseline=JSON.parse(fs.readFileSync(new URL('BASELINE_1_2_0.json',root)));
 assert.equal(Object.keys(baseline.tables).length,21);
 for(const [t,rows] of Object.entries(baseline.tables))for(const r of rows){
  const current=d[t].find(x=>x[r.primary_key]===r.id);assert(current,`${t}:${r.id}`);
  const projection=Object.fromEntries(r.keys.map(k=>[k,current[k]]));
  assert.equal(crypto.createHash('sha256').update(JSON.stringify(canonical(projection))).digest('hex'),r.sha256,`${t}:${r.id}`);
 }
});
test('every scaling record has all twelve fields with provenance or explicit unknown',()=>{
 for(const p of phase.profiles){
  const fields=d.assertions.filter(x=>x.system_id===p.system_id);assert.equal(fields.length,12);
  for(const f of fields)if(f.evidence_status!=='Not verified')assert(recordEvidence(d,'assertions',f.assertion_id).length);
  else assert.match(f.value,/n.a.;/);
  assert(d.deployments.some(x=>x.system_id===p.system_id&&/not actual go-live/.test(x.date_precision)));
 }
});
test('all 78 newly used source records expose successful excerpt-membership and extraction basis',()=>{
 const audit=JSON.parse(fs.readFileSync(new URL('SCALING_QUOTE_AUDIT.json',root)));
 assert.equal(audit.length,78);assert.equal(d.sources.filter(s=>s.source_id.startsWith('grow-')).length,78);
 for(const row of audit){assert(row.all_selected_passages_match);assert(row.selected_words<=250);assert.match(row.fetched_text_sha256,/^[a-f0-9]{64}$/);assert(row.retrieval_basis);}
 assert(audit.some(r=>/recovery/i.test(r.retrieval_basis)));
});
test('new excerpt budgets aggregate original URLs including historical catalogue versions',()=>{
 const urls=new Set(phase.sources.map(s=>s.url));
 for(const url of urls){
  const ids=new Set(d.sources.filter(s=>s.url===url).map(s=>s.source_id));
  const quotes=new Set(d.evidence.filter(e=>ids.has(e.source_id)).map(e=>e.quote));
  assert([...quotes].join(' ').split(/\s+/).length<=250,url);
 }
});
test('scaling search and retrieval retain failures, cached recovery and no full copied pages',()=>{
 const q=JSON.parse(fs.readFileSync(new URL('SCALING_SEARCH.json',root)));
 const r=JSON.parse(fs.readFileSync(new URL('SCALING_RETRIEVAL.json',root)));
 assert.equal(q.queries.length,591);assert.equal(q.hits.length,2511);assert.equal(q.errors.length,0);
 assert.equal(r.length,228);assert.equal(r.filter(x=>x.error).length,41);
 assert(r.some(x=>x.is_cached));assert(r.every(x=>!x.content&&!x.snippet));
});
test('original recheck is not falsely extended to all new assertions',()=>{
 assert.equal(d.source_rechecks.length,50);assert.equal(d.assertion_rechecks.length,216);
 assert(!d.assertion_rechecks.some(r=>phase.profiles.some(p=>p.system_id===r.system_id)));
});
test('MuleHunter bank-local privacy is not a blanket intelligence-sharing guarantee',()=>{
 assert.match(a('sys-mulehunter','Privacy & retention').value,/Separate May 2026/);
 assert.match(a('sys-mulehunter','Privacy & retention').value,/suspect identifiers/);
 assert(d.issues.some(i=>i.system_id==='sys-mulehunter'&&i.issue_type.includes('intelligence')));
 assert.match(a('sys-mulehunter','Deployment & date').value,/hourly/);
});
test('Poshan completion metric and cache deletion do not become accuracy or server retention',()=>{
 const m=d.metrics.find(x=>x.system_id==='sys-poshan-frs');assert.equal(m.value,97.01);
 assert.equal(m.metric_kind,'Administrative completion self-report');
 assert.match(a('sys-poshan-frs','Privacy & retention').value,/does not establish server retention/);
});
test('Adalat mandate preserves officer fallback and does not certify universal acceptance',()=>{
 assert.match(a('sys-adalat-ai','Current-status limits').value,/not verified universal use/);
 assert.match(a('sys-adalat-ai','Human review & overrides').value,/fallback/);
 assert(d.system_policy_links.some(x=>x.system_id==='sys-adalat-ai'));
});
test('CAG pension controls remain procurement requirements not observed enforcement',()=>{
 assert.match(a('sys-cag-paras','Human review & overrides').value,/requires/);
 assert.match(a('sys-cag-paras','Privacy & retention').value,/requirement, not observed/);
 assert.match(a('sys-cag-paras','Procurement & supplier').value,/not executed award/);
});
test('BharatGen programme support is not broader mission outlay or reconciled spending',()=>{
 const p=d.procurements.find(p=>p.system_id==='sys-bharatgen');
 assert.equal(p.amount_inr,2350000000);assert.match(p.amount_type,/not reconciled/);
 assert.match(a('sys-bharatgen','Funding & contract').value,/broader IndiaAI Mission/);
});
test('Shiksha Copilot evaluation retains partner abstract-only and non-causal limitations',()=>{
 const e=d.evaluations.find(x=>x.system_id==='sys-shiksha-copilot');assert.equal(e.sample_n,1043);
 assert.match(e.evaluation_type,/abstract reviewed only/);
 assert.match(a('sys-shiksha-copilot','Evaluation & error rates').value,/not independent causal/);
 assert.match(a('sys-shiksha-copilot','Human review & overrides').value,/teachers customise/);
});
test('Nagpur equipment installation and Goa announcement chronology remain qualified',()=>{
 assert.match(d.systems.find(s=>s.system_id==='sys-nagpur-iitms').stage,/integration unfinished/);
 assert.match(a('sys-nagpur-iitms','Current-status limits').value,/does not prove/);
 assert.match(d.systems.find(s=>s.system_id==='sys-goa-online-ai').stage,/February 2026 beta/);
 assert.match(a('sys-goa-online-ai','Deployment & date').value,/precedes September/);
});
test('family coalescing and homonym disambiguation prevent artificial count inflation',()=>{
 assert.equal(d.systems.filter(s=>s.system_id.startsWith('sys-bharatgen')).length,1);
 assert.equal(d.systems.filter(s=>/CA GPT family/.test(s.name)).length,1);
 assert.equal(d.systems.filter(s=>/TRINETRA cybersecurity/.test(s.name)).length,1);
 assert(d.systems.some(s=>s.system_id==='sys-yaksh'));
 assert(d.candidate_decisions.some(c=>c.name==='Rajasthan eMitra AI assistant'));
 assert(!d.systems.some(s=>s.system_id==='sys-emitra-ai'||s.system_id==='sys-robot-sentry'));
});
test('defence catalogue capabilities have correct institutional responsibility',()=>{
 for(const [sid,pattern] of [['sys-army-ims',/Indian Army/],['sys-beml-fatigue',/BEML/],['sys-navy-afib',/Indian Navy/],['sys-grse-anvesha',/Garden Reach/]]){
  const s=d.systems.find(s=>s.system_id===sid);assert.match(d.institutions.find(i=>i.institution_id===s.owner_institution_id).name,pattern);
 }
 assert.equal(d.systems.find(s=>s.system_id==='sys-muntra').ai_class,'Qualified algorithmic / biometric context');
});
test('latest study contains every addition and its twelve-field unknowns',()=>{
 const text=fs.readFileSync(new URL('SCALING_STUDY.md',root),'utf8');
 for(const p of phase.profiles){assert(text.includes('### '+p.name));assert(text.includes(p.system_id));}
 assert(text.includes('not 144 verified live AI deployments'));
 assert.equal((text.match(/\*\*Funding evidence /g)||[]).length,72);
});
test('cohort combinations, exports and original frame denominator agree',()=>{
 assert.equal(filterSystems(d,{cohort:'1.3.0',frame:'Outside frame'}).length,72);
 assert.equal(filterSystems(d,{cohort:'1.3.0',frame:'frame-health'}).length,0);
 const csv=registryCsv(d,filterSystems(d,{cohort:'1.3.0'}));
 assert.equal(csv.trim().split(/\r?\n/).length,73);assert(csv.includes('research_round'));assert(csv.includes('system_kind'));
 assert.equal(d.coverage_systems.length,26);
});
test('research provenance and new downloadable study are visible in the application',()=>{
 const app=fs.readFileSync(new URL('../src/Registry.tsx',import.meta.url),'utf8');
 for(const s of ['registry-filter-cohort','SCALING_STUDY.md','SCALING_QUOTE_AUDIT.json','Cached extraction','144 independently verified live AI'])assert(app.includes(s));
});
