import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';
const d=JSON.parse(readFileSync(new URL('../src/data/policy.json',import.meta.url)));
assert.equal(d.provisions.length,30);assert.equal(d.corrections.length,8);assert.equal(d.sources.length,4);
for(const p of d.provisions){
  for(const key of ['id','label','title','summary','interpretation','question','caution','draftText','finalText','correctedText','beforeExcerpt','afterExcerpt'])assert.ok(typeof p[key]==='string'&&p[key].length>0,`${p.id}: ${key}`);
  assert.ok(p.draftPage>0&&p.finalPage>0);
}
console.log('PASS: 30 complete records, 8 corrections, 4 source objects.');
