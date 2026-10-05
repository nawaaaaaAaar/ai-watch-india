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
