import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';
import {mergeCollections} from '../src/lib.mjs';
const d=JSON.parse(readFileSync(new URL('../src/data/policy.json',import.meta.url)));
assert.equal(d.provisions.length,30);assert.equal(d.corrections.length,8);assert.equal(d.sources.length,4);
for(const p of d.provisions){
  for(const key of ['id','label','title','summary','interpretation','question','caution','draftText','finalText','correctedText','beforeExcerpt','afterExcerpt'])assert.ok(typeof p[key]==='string'&&p[key].length>0,`${p.id}: ${key}`);
  assert.ok(p.draftPage>0&&p.finalPage>0);
}
console.log('PASS: 30 complete records, 8 corrections, 4 source objects.');
const e=JSON.parse(readFileSync(new URL('../src/data/expansion.json',import.meta.url)));
const combined=mergeCollections(d,e);
assert.equal(combined.provisions.length,56);assert.equal(combined.sources.length,13);
assert.equal(combined.corrections.length,10);assert.equal(combined.provisions.filter(p=>p.contribution).length,30);
for(const p of e.provisions){
  assert.ok(p.familyId&&p.draftUrl&&p.finalUrl&&p.draftLocator&&p.finalLocator&&p.legalStatus);
  assert.ok(p.draftText.includes(p.beforeExcerpt)&&p.finalText.includes(p.afterExcerpt));
}
console.log('PASS: expanded collection has 56 records, 30 briefs, 13 sources and 10 English corrections.');
const implementation=JSON.parse(readFileSync(new URL('../src/data/implementation.json',import.meta.url)));
const editionThree=mergeCollections(d,e,implementation);
assert.equal(editionThree.provisions.length,66);assert.equal(editionThree.sources.length,25);
assert.equal(editionThree.provisions.filter(p=>p.contribution).length,40);
for(const p of implementation.provisions){
  assert.ok(p.implementationCheckpoint&&p.evidenceStatus&&p.relatedId);
  assert.ok(p.evidenceTrail.length>=2&&p.requestChecklist.length>=3);
  assert.ok(p.correctionIds.length===0&&p.type==='Evidence checkpoint');
}
console.log('PASS: edition three has 66 evidence units, 40 briefs and 25 sources.');
const service=JSON.parse(readFileSync(new URL('../src/data/public-services.json',import.meta.url)));
const editionFour=mergeCollections(d,e,implementation,service);
assert.equal(editionFour.provisions.length,72);assert.equal(editionFour.sources.length,40);
assert.equal(editionFour.provisions.filter(p=>p.contribution).length,46);
assert.equal(editionFour.families.length,5);assert.equal(editionFour.corrections.length,10);
for(const p of service.provisions){
  assert.ok(p.publicServiceCase&&p.sector&&p.deploymentStage);
  assert.deepEqual(p.caseFields.map(f=>f.name),service.dimensions);
  for(const f of p.caseFields){assert.ok(f.statement&&f.status);if(f.status==='Documented')assert.ok(f.evidence.length);}
}
console.log('PASS: edition four has 72 evidence units, 46 briefs, 40 sources and all 72 case dimension slots.');
