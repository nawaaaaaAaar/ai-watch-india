import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {mergeCollections,evidenceLinks,filterProvisions,createBrief,csv,validateNotebook,FINAL_URL,SGI_FINAL,SGI_CORRECTION} from '../src/lib.mjs';
const original=JSON.parse(readFileSync(new URL('../src/data/policy.json',import.meta.url)));
const expansion=JSON.parse(readFileSync(new URL('../src/data/expansion.json',import.meta.url)));
const data=mergeCollections(original,expansion);
const p=id=>data.provisions.find(p=>p.id===id);
const norm=s=>s.replace(/\s+/g,' ').trim();
test('three collections contain 56 unique records',()=>{
  assert.equal(data.families.length,3);assert.equal(data.provisions.length,56);
  assert.equal(new Set(data.provisions.map(p=>p.id)).size,56);
  for(const [id,count] of [['dpdp',30],['sgi',14],['aig',12]])assert.equal(data.provisions.filter(p=>p.familyId===id).length,count);
});
test('all original DPDP wording and IDs remain unchanged',()=>{
  for(const record of original.provisions){const newer=p(record.id);for(const key of ['draftText','finalText','correctedText','beforeExcerpt','afterExcerpt'])assert.equal(newer[key],record[key]);}
});
test('contribution counts are 12 original plus 10 SGI plus 8 AI',()=>{
  assert.equal(data.provisions.filter(p=>p.contribution).length,30);
  for(const [family,count] of [['dpdp',12],['sgi',10],['aig',8]])assert.equal(data.provisions.filter(p=>p.contribution&&p.familyId===family).length,count);
});
test('thirteen snapshots retain their SHA-256 values',()=>{
  assert.equal(data.sources.length,13);
  for(const s of data.sources)assert.equal(createHash('sha256').update(readFileSync(new URL('../public/'+s.snapshot,import.meta.url))).digest('hex'),s.hash);
});
test('every expansion quote is present in its real source snapshot',()=>{
  for(const record of expansion.provisions){
    for(const [side,key] of [['before','beforeExcerpt'],['after','afterExcerpt']]){
      const src=data.sources.find(s=>s.id===record[`${side}SourceId`]);
      const text=norm(readFileSync(new URL('../public/'+src.snapshot,import.meta.url),'utf8'));
      assert.ok(text.includes(record[key]),record.id+' '+side);
    }
  }
});
test('all mapped expansion segments are present in the source snapshots',()=>{
  for(const record of expansion.provisions){
    for(const [idKey,textKey] of [['beforeSourceId','draftText'],['afterSourceId','finalText']]){
      const src=data.sources.find(s=>s.id===record[idKey]);
      const text=norm(readFileSync(new URL('../public/'+src.snapshot,import.meta.url),'utf8'));
      assert.ok(text.includes(record[textKey]),record.id+' '+textKey);
    }
  }
});
test('SGI adds two localized English corrections, not Hindi substitutions',()=>{
  assert.equal(data.corrections.length,10);assert.equal(expansion.corrections.length,2);
  assert.deepEqual(p('sgi-user-notices').correctionIds,['SGI-CR-01','SGI-CR-02']);
  assert.equal((p('sgi-user-notices').correctedText.match(/read with the Bharatiya/g)||[]).length,2);
  assert.equal((p('sgi-user-notices').finalText.match(/read with the Bharatiya/g)||[]).length,0);
  for(const record of expansion.provisions.filter(p=>p.id!=='sgi-user-notices'))assert.equal(record.correctedText,record.finalText);
});
test('changes absent from the draft point to previous law, not invented draft quotes',()=>{
  for(const id of ['sgi-user-notices','sgi-takedown','sgi-grievance','sgi-proactive','sgi-criminal']){
    assert.equal(p(id).comparisonKind,'Prior law to amended law');
    assert.equal(p(id).beforeSourceId,'sgi-baseline');
    assert.match(evidenceLinks(p(id)).before,/708f6a/);
  }
});
test('SGI definition and exclusions retain material conditions',()=>{
  assert.match(p('sgi-definition').afterExcerpt,/audio, visual or audio-visual/);
  assert.match(p('sgi-exclusions').afterExcerpt,/does not materially alter/);
  assert.match(p('sgi-exclusions').finalText,/false document or false electronic record/);
});
test('SGI ten-percent removal retains prominent disclosure and feasible provenance',()=>{
  assert.match(p('sgi-label').beforeExcerpt,/ten percent/);assert.doesNotMatch(p('sgi-label').afterExcerpt,/ten percent/);
  assert.match(p('sgi-label').afterExcerpt,/prominently prefixed audio/);
  assert.match(p('sgi-provenance').afterExcerpt,/to the extent technically feasible/);
});
test('AI comparisons are recommendation lineage, not new legal mandates',()=>{
  for(const record of expansion.provisions.filter(p=>p.familyId==='aig')){
    assert.equal(record.comparisonKind,'Recommendation lineage');
    assert.match(record.legalStatus,/Recommendations/);
    assert.match(record.caution,/not a one-to-one legal/);
  }
});
test('printed AI locators do not invent PDF page fragments',()=>{
  for(const record of expansion.provisions.filter(p=>p.familyId==='aig')){
    assert.doesNotMatch(evidenceLinks(record).after,/#page=/);assert.match(record.finalLocator,/printed pp?/);
  }
});
test('family filters and cross-family search work',()=>{
  for(const [family,count] of [['dpdp',30],['sgi',14],['aig',12]])assert.equal(filterProvisions(data.provisions,'','All','All',family).length,count);
  assert.ok(filterProvisions(data.provisions,'incidents','All','All','aig').some(x=>x.id==='aig-incidents'));
  assert.equal(filterProvisions(data.provisions,'no-such-evidence','All','All','sgi').length,0);
});
test('AI-only exports use AI sources, no DPDP timing boilerplate',()=>{
  const out=createBrief(data,{title:'AI',selected:['aig-incidents'],reviews:[]});
  assert.match(out,/recommendation lineage/i);assert.match(out,/subcommittee-report-dec26/);
  assert.match(out,/doc2025115685601/);assert.ok(!out.includes(FINAL_URL));
  assert.doesNotMatch(out,/13\/14 November publication-date basis/);
});
test('mixed-family exports retain correct citations and legal status',()=>{
  const out=createBrief(data,{title:'Mixed',selected:['rule-8','sgi-user-notices','aig-voluntary'],reviews:[]});
  for(const url of [FINAL_URL,SGI_FINAL,SGI_CORRECTION])assert.ok(out.includes(url));
  assert.match(out,/Prior law to amended law/);assert.match(out,/not a new standalone legal mandate/);
  const table=csv([p('sgi-takedown'),p('aig-voluntary')]);
  assert.match(table,/708f6a/);assert.match(table,/doc2025115685601/);
});
test('old notebooks remain compatible and expanded selections round-trip',()=>{
  const ids=data.provisions.map(p=>p.id);
  const old={version:1,title:'Old',selected:['rule-8'],reviews:[]};
  assert.deepEqual(validateNotebook(old,ids),old);
  const all={version:1,title:'All',selected:ids,reviews:[]};
  assert.equal(validateNotebook(all,ids).selected.length,56);
});
test('all thirty packaged briefs and three family bundles are source-backed',()=>{
  for(const record of data.provisions.filter(p=>p.contribution)){
    const text=readFileSync(new URL('../public/briefs/'+record.id+'.md',import.meta.url),'utf8');
    assert.ok(text.includes(evidenceLinks(record).after));assert.match(text,/Limits and follow-up/);
  }
  for(const family of data.families)assert.ok(readFileSync(new URL('../public/briefs/'+family.id+'-contributions.md',import.meta.url),'utf8').length>10000);
});
test('combined downloadable data equals the application merge',()=>{
  assert.deepEqual(JSON.parse(readFileSync(new URL('../public/combined-data.json',import.meta.url))),data);
});
