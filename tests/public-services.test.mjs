import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {mergeCollections,createBrief,csv,accountabilityCsv,filterProvisions,validateNotebook} from '../src/lib.mjs';
const read=name=>JSON.parse(readFileSync(new URL(`../src/data/${name}.json`,import.meta.url)));
const prior=['policy','expansion','implementation'].map(read), service=read('public-services');
const data=mergeCollections(...prior,service,read('context')), old=mergeCollections(...prior);
const get=id=>service.provisions.find(p=>p.id===`service-${id}`);
const brief=p=>createBrief(data,{version:1,title:'Case',selected:[p.id],reviews:[]},'5 October 2026');
const norm=t=>t.replace(/\s+/g,' ').trim();
test('current corpus has five collections, 72 units, 46 briefs, 46 sources and ten corrections',()=>{
  assert.equal(data.families.length,5);assert.equal(data.provisions.length,72);assert.equal(data.sources.length,46);
  assert.equal(data.provisions.filter(p=>p.contribution).length,46);assert.equal(data.corrections.length,10);
  assert.equal(new Set(data.provisions.map(p=>p.id)).size,72);assert.equal(new Set(data.sources.map(s=>s.id)).size,46);
});
test('all prior 66 records and 25 sources remain byte-value equivalent',()=>{
  assert.deepEqual(data.provisions.slice(0,66),old.provisions);assert.deepEqual(data.sources.slice(0,25),old.sources);
  assert.deepEqual(data.corrections,old.corrections);
});
test('six cases retain exactly the same twelve dimensions including unknowns',()=>{
  assert.equal(service.provisions.length,6);
  for(const p of service.provisions){
    assert.deepEqual(p.caseFields.map(f=>f.name),service.dimensions);
    assert.ok(p.publicServiceCase&&p.contribution&&p.sector&&p.deploymentStage);
    assert.equal(p.type,'Public-service case');assert.equal(p.correctionIds.length,0);
    assert.ok(p.requestChecklist.length>=5);
  }
});
test('evidence statuses are bounded and missing dimension values are explicit',()=>{
  for(const p of service.provisions)for(const f of p.caseFields){
    assert.ok(['Documented','Partial','Not verified','Conflicting sources'].includes(f.status));
    assert.ok(f.statement.length>20);
    if(!f.evidence.length){assert.equal(f.status,'Not verified');assert.match(f.statement,/n\.a\./);}
    if(f.status==='Documented')assert.ok(f.evidence.length);
  }
});
test('twenty selected snapshots have matching hashes and source type labels',()=>{
  assert.equal(service.sources.length,20);
  for(const s of service.sources){
    const bytes=readFileSync(new URL('../public/'+s.snapshot,import.meta.url));
    assert.equal(createHash('sha256').update(bytes).digest('hex'),s.hash);
    assert.equal(s.snapshotKind,'Selected excerpts');assert.ok(s.sourceType);
    assert.match(bytes.toString(),/not a full document archive/);
    const quotes=bytes.toString().split('\n\n').slice(1).join(' ').trim();
    assert.ok(quotes.split(/\s+/).length<=250,s.id);
  }
});
test('all field quotations, URLs and locators resolve to exact source excerpts',()=>{
  for(const p of service.provisions)for(const f of p.caseFields)for(const e of f.evidence){
    const s=data.sources.find(s=>s.id===e.sourceId);assert.ok(s);
    assert.equal(e.url,s.url);assert.ok(e.locator);
    assert.ok(norm(readFileSync(new URL('../public/'+s.snapshot,import.meta.url),'utf8')).includes(norm(e.quote)),e.sourceId);
  }
});
test('all public-service sources are actually cited by a case',()=>{
  const used=new Set(service.provisions.flatMap(p=>p.evidenceTrail.map(e=>e.sourceId)));
  for(const s of service.sources)assert.ok(used.has(s.id),s.id);
});
test('UPSC preserves historical procurement versus current application boundary',()=>{
  const p=get('upsc');assert.match(p.caution,/2024.*2026/);
  assert.match(p.caseFields[3].statement,/contract link.*unverified/);
  assert.match(p.caseFields[8].statement,/Applying it.*not established/);
  assert.match(p.caseFields[6].statement,/false-accept\/reject/);
});
test('I4C winner table is not labelled an executed production award',()=>{
  const p=get('cyberguard');assert.match(p.caseFields[3].statement,/not verified/);
  assert.ok(p.evidenceTrail.some(e=>e.sourceId==='impl-mission-status'));
  assert.match(p.interpretation,/do not establish.*FIR/);
});
test('SUVAS local human review is not made a universal court SOP',()=>{
  const p=get('suvas');assert.match(p.caution,/jurisdiction-specific and historical/);
  assert.match(p.caseFields[7].statement,/local, not universal/);
});
test('SUPACE remains experimental and court consultation remains a draft',()=>{
  const p=get('supace');assert.match(p.deploymentStage,/Experimental/);
  assert.match(p.summary,/experimental and not yet used regularly/);
  assert.match(p.caution,/consultation draft.*not verified enacted/);
});
test('health local study accuracy is not transferred to national deployed CDSS',()=>{
  const p=get('esanjeevani');assert.match(p.caseFields[6].statement,/not the existing national system/);
  assert.match(p.caseFields[11].statement,/not a deployed-CDSS accuracy study/);
  assert.match(p.interpretation,/not evidence of an autonomous diagnosis/);
});
test('health retention exception and privacy-only contact remain visible',()=>{
  const p=get('esanjeevani');assert.match(p.caseFields[8].statement,/excludes medical reports\/diagnoses/);
  assert.match(p.caseFields[9].statement,/clinical-error.*not verified/);
});
test('policing pilot count tension and announced-not-completed scale preserved',()=>{
  const p=get('mahacrimeos');assert.equal(p.caseFields[2].status,'Conflicting sources');
  assert.match(p.caseFields[2].statement,/23 and 25/);assert.match(p.caseFields[2].statement,/completed.*not verified/);
  assert.equal(data.sources.find(s=>s.id==='service-police-vendor').sourceType,'Vendor account');
  assert.equal(data.sources.find(s=>s.id==='service-police-reporting').sourceType,'News reporting');
});
test('case search covers accountability statements and evidence',()=>{
  assert.deepEqual(filterProvisions(data.provisions,'device deletion','All','All','service').map(p=>p.id),[]);
  assert.ok(filterProvisions(data.provisions,'retention','All','All','service').length>=5);
  assert.equal(filterProvisions(data.provisions,'','Public-service case').length,6);
});
test('Markdown preserves every dimension, status, evidence URL and checklist',()=>{
  for(const p of service.provisions){
    const out=brief(p);for(const f of p.caseFields){assert.ok(out.includes('#### '+f.name));assert.ok(out.includes(f.statement));}
    for(const e of p.evidenceTrail)assert.ok(out.includes(e.url));
    for(const x of p.requestChecklist)assert.ok(out.includes(x));
    assert.match(out,/System evidence trail/);
  }
});
test('case-only provenance excludes unrelated case source records and DPDP timing',()=>{
  const out=brief(get('upsc'));assert.doesNotMatch(out,/DPDP: the official rule/);
  assert.doesNotMatch(out,/Microsoft CrimeOS customer story/);assert.match(out,/UPSC biometric\/AI tender/);
});
test('accountability CSV retains all 72 rows and links, with formula escaping',()=>{
  const out=accountabilityCsv(service.provisions);assert.equal(out.split('\r\n').length,73);
  assert.match(out,/Evaluation & error rates/);assert.match(out,/https:\/\/www.pib.gov.in/);
  const dangerous=structuredClone(get('upsc'));dangerous.caseFields[0].statement='=1+1';
  assert.match(accountabilityCsv([dangerous]),/"'=1\+1"/);
  assert.match(csv(service.provisions),/Accountability fields \(JSON\)/);
});
test('all 72-unit notebooks and mixed five-collection exports remain compatible',()=>{
  const book={version:1,title:'All',selected:data.provisions.map(p=>p.id),reviews:[]};
  assert.equal(validateNotebook(book,book.selected).selected.length,72);
  const out=createBrief(data,book);assert.match(out,/Complete accountability matrix/);assert.match(out,/DPDP:/);assert.match(out,/Implementation evidence:/);
});
test('packaged case briefs, matrix and complete dataset reproduce the app',()=>{
  for(const p of service.provisions){
    const out=readFileSync(new URL('../public/briefs/'+p.id+'.md',import.meta.url),'utf8');
    assert.match(out,/Complete accountability matrix/);assert.match(out,/Current-status limits/);
  }
  assert.equal(readFileSync(new URL('../public/research/public-service-coverage.csv',import.meta.url),'utf8'),accountabilityCsv(service.provisions));
  assert.deepEqual(JSON.parse(readFileSync(new URL('../public/combined-data.json',import.meta.url))),data);
});
