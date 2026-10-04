import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {filterProvisions, validateNotebook, createBrief, csv, DRAFT_URL, FINAL_URL, CORRECTION_URL, ACT_URL} from '../src/lib.mjs';
const data=JSON.parse(readFileSync(new URL('../src/data/policy.json',import.meta.url)));
const p=id=>data.provisions.find(x=>x.id===id);
test('complete final inventory: 23 rules, 7 schedules, no duplicate IDs',()=>{
  assert.equal(data.provisions.length,30);assert.equal(data.provisions.filter(p=>p.id.startsWith('rule-')).length,23);
  assert.equal(new Set(data.provisions.map(p=>p.id)).size,30);
});
test('all source records have verified extracted-text hashes',()=>{
  for(const s of data.sources){const text=readFileSync(new URL('../public/'+s.snapshot,import.meta.url));assert.equal(createHash('sha256').update(text).digest('hex'),s.hash);assert.match(s.hashType,/not original PDF/);}
});
test('focused quotes match the as-printed text',()=>{
  for(const r of data.provisions){assert.ok(r.draftText.includes(r.beforeExcerpt),r.id);assert.ok(r.finalText.includes(r.afterExcerpt),r.id);}
});
test('split disability/child rules both map to draft rule 10',()=>{
  assert.match(p('rule-10').draftLabel,/rule 10/i);assert.match(p('rule-11').draftLabel,/rule 10/i);
});
test('retention finding distinguishes minimum floor and security-purpose retention',()=>{
  assert.match(p('rule-8').afterExcerpt,/minimum period of one year/);assert.match(p('rule-8').interpretation,/security-purpose/);
});
test('individual breach location deleted while Board location retained',()=>{
  assert.match(p('rule-7').beforeExcerpt,/location/);assert.doesNotMatch(p('rule-7').afterExcerpt,/location/);
  assert.match(p('rule-7').finalText,/timing and location/);
});
test('official corrections are localized and print preserved',()=>{
  assert.equal(data.corrections.length,8);
  assert.match(p('rule-1').finalText,/of this Gazette/);assert.doesNotMatch(p('rule-1').correctedText,/of this Gazette/);
  assert.match(p('rule-23').correctedText,/given in such order/);
  assert.match(p('schedule-first').correctedText,/every body corporate/);
  assert.match(p('schedule-fourth').correctedText,/\(g\) “mental health/);
  assert.match(p('schedule-fourth').finalText,/\(f\) “mental health/);
});
test('filtering searches all records and supports combined constraints',()=>{
  assert.equal(filterProvisions(data.provisions).length,30);
  assert.equal(filterProvisions(data.provisions,'definitely-no-match').length,0);
  assert.ok(filterProvisions(data.provisions,'retention').some(x=>x.id==='rule-8'));
  assert.deepEqual(filterProvisions(data.provisions,'','Addition','Data Principals').map(x=>x.id),['rule-14']);
});
test('Markdown brief retains citations, interpretation, caveats and notes',()=>{
  const out=createBrief(data,{title:'Test',selected:['rule-8','rule-23'],reviews:[{provisionId:'rule-8',reviewer:'Test reviewer',note:'Checked quote',status:'checked',timestamp:'2026-10-04T21:00:00Z'}]});
  for(const url of [DRAFT_URL,FINAL_URL,CORRECTION_URL,ACT_URL])assert.ok(out.includes(url));
  assert.match(out,/publication-date basis is unresolved/);assert.match(out,/Local review history/);assert.match(out,/Checked quote/);
});
test('notebook validation rejects wrong version, bad IDs, duplicated IDs and forged state',()=>{
  const valid={version:1,title:'Brief',selected:['rule-8'],reviews:[]};
  assert.deepEqual(validateNotebook(valid,data.provisions.map(x=>x.id)),valid);
  for(const bad of [{...valid,version:2},{...valid,selected:['missing']},{...valid,selected:['rule-8','rule-8']},{...valid,reviews:[{provisionId:'rule-8',reviewer:'',note:'x',status:'approved',timestamp:'invalid'}]}])assert.throws(()=>validateNotebook(bad,data.provisions.map(x=>x.id)));
});
test('CSV escapes quotes and neutralizes spreadsheet formulas',()=>{
  const out=csv([{...p('rule-8'),title:'=1+1',summary:'Text "quoted"'}]);
  assert.match(out,/'=1\+1/);assert.match(out,/"Text ""quoted"""/);
});
test('twelve distinct contribution briefs are complete and source-linked',()=>{
  const ids=['rule-8','rule-14','rule-13','schedule-fourth','rule-7','rule-11','schedule-second','rule-1','rule-6','rule-3','rule-15','rule-23'];
  assert.equal(new Set(ids).size,12);
  for(const id of ids){const text=readFileSync(new URL('../public/briefs/'+id+'.md',import.meta.url),'utf8');assert.ok(text.includes(FINAL_URL));assert.match(text,/Analyst interpretation/);assert.match(text,/Limits and follow-up/);}
});
