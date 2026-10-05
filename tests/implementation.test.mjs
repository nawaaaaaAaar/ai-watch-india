import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {mergeCollections,createBrief,filterProvisions,validateNotebook,csv} from '../src/lib.mjs';
const load=name=>JSON.parse(readFileSync(new URL('../src/data/'+name+'.json',import.meta.url)));
const original=load('policy'),expansion=load('expansion'),implementation=load('implementation');
const data=mergeCollections(original,expansion,implementation);
const p=id=>implementation.provisions.find(p=>p.id===id);
const norm=text=>text.replace(/\s+/g,' ').trim();
test('edition three contains four collections, 66 units, 40 briefs, 25 sources',()=>{
  assert.equal(data.families.length,4);assert.equal(data.provisions.length,66);
  assert.equal(data.provisions.filter(p=>p.contribution).length,40);assert.equal(data.sources.length,25);
  assert.equal(new Set(data.provisions.map(p=>p.id)).size,66);assert.equal(data.corrections.length,10);
});
test('all original and edition-two source wording remains untouched',()=>{
  const old=mergeCollections(original,expansion);
  assert.deepEqual(data.provisions.slice(0,56),old.provisions);
  assert.deepEqual(data.sources.slice(0,13),old.sources);
});
test('implementation snapshots retain twelve recorded integrity hashes',()=>{
  assert.equal(implementation.sources.length,12);
  for(const s of implementation.sources){
    const bytes=readFileSync(new URL('../public/'+s.snapshot,import.meta.url));
    assert.equal(createHash('sha256').update(bytes).digest('hex'),s.hash);
  }
});
test('every trail quote is a real exact normalized source excerpt',()=>{
  for(const record of implementation.provisions){
    assert.ok(record.evidenceTrail.length>=2);assert.equal(record.type,'Evidence checkpoint');
    for(const e of record.evidenceTrail){
      const s=data.sources.find(s=>s.id===e.sourceId);
      assert.ok(s);assert.equal(s.url,e.url);
      const text=norm(readFileSync(new URL('../public/'+s.snapshot,import.meta.url),'utf8'));
      assert.ok(text.includes(e.quote),record.id+' '+e.sourceId);
    }
  }
});
test('recommendation cross-references resolve to existing guideline records',()=>{
  for(const record of implementation.provisions){
    const related=data.provisions.find(p=>p.id===record.relatedId);
    assert.equal(related.familyId,'aig');
    const guidelines=norm(readFileSync(new URL('../public/snapshots/aig-guidelines.txt',import.meta.url),'utf8'));
    assert.ok(guidelines.includes(record.beforeExcerpt));
    assert.equal(record.draftUrl,related.finalUrl);
  }
});
test('constitution dates remain distinct from announcement dates',()=>{
  assert.equal(data.sources.find(s=>s.id==='impl-aigeg-order').documentDate,'13 April 2026');
  assert.equal(data.sources.find(s=>s.id==='impl-aigeg-release').documentDate,'16 April 2026');
  assert.equal(data.sources.find(s=>s.id==='impl-tpec-release').documentDate,'18 April 2026');
});
test('Safety Institute wording tension retains both official statements',()=>{
  assert.match(p('impl-aisi-status').evidenceTrail[0].quote,/has been established/);
  assert.match(p('impl-aisi-status').evidenceTrail[1].quote,/is being established/);
  assert.match(p('impl-aisi-status').caution,/different stages/);
});
test('historical recruitment and call do not imply open opportunities or awards',()=>{
  assert.match(p('impl-aisi-leadership').caution,/not an open job listing/);
  assert.match(p('impl-aisi-partners').caution,/expired EOI/);
  assert.match(p('impl-aisi-partners').evidenceTrail[1].quote,/50%/);
});
test('portfolio approvals and tool selections do not imply proven performance',()=>{
  assert.match(p('impl-projects').interpretation,/not completion/);
  assert.match(p('impl-tool-delivery').caution,/predates/);
  assert.match(p('impl-tool-delivery').interpretation,/does not establish accuracy/);
});
test('repository evidence gap is bounded and distinct from cyber duties',()=>{
  const record=p('impl-incident-repository');
  assert.match(record.caution,/not proof of absence/);
  assert.match(record.caution,/not a universal deadline/);
  assert.match(record.evidenceTrail[1].quote,/6 hours/);
  assert.match(record.evidenceTrail[2].quote,/Machine Learning/);
});
test('redress and voluntary commitments preserve scope limits',()=>{
  assert.match(p('impl-redress').interpretation,/not an all-purpose appeal/);
  assert.match(p('impl-voluntary').caution,/not every signatory/);
});
test('implementation filtering does not mix in policy comparisons',()=>{
  assert.equal(filterProvisions(data.provisions,'','All','All','impl').length,10);
  assert.equal(filterProvisions(data.provisions,'','Evidence checkpoint').length,10);
  assert.ok(filterProvisions(data.provisions,'recruitment','All','All','impl').length>0);
});
test('implementation brief includes every trail item, checklist and source provenance',()=>{
  const record=p('impl-aisi-status');
  const out=createBrief(data,{title:'Implementation',selected:[record.id],reviews:[]});
  for(const e of record.evidenceTrail)assert.ok(out.includes(e.quote)&&out.includes(e.url));
  assert.match(out,/Records to request or verify/);assert.match(out,/not a filed information request/);
  assert.match(out,/doc2025115685601/);assert.doesNotMatch(out,/13\/14 November/);
});
test('mixed four-family exports and version-one notebooks remain usable',()=>{
  const selected=['rule-8','sgi-label','aig-institutions','impl-tpec'];
  const book={version:1,title:'Mixed',selected,reviews:[]};
  assert.deepEqual(validateNotebook(book,data.provisions.map(p=>p.id)),book);
  const out=createBrief(data,book);assert.match(out,/constitution-of-tpec/);assert.match(out,/Synthetic media/);
  assert.match(csv(selected.map(id=>data.provisions.find(p=>p.id===id))),/Evidence checkpoint/);
});
test('all ten packaged checkpoint briefs include trail and request checklist',()=>{
  for(const record of implementation.provisions){
    const text=readFileSync(new URL('../public/briefs/'+record.id+'.md',import.meta.url),'utf8');
    assert.match(text,/Implementation evidence trail/);assert.match(text,/Records to request or verify/);
    for(const e of record.evidenceTrail)assert.ok(text.includes(e.url));
  }
});
test('full notebook inventory and combined export match 66-unit application data',()=>{
  const book={version:1,title:'All',selected:data.provisions.map(p=>p.id),reviews:[]};
  assert.equal(validateNotebook(book,book.selected).selected.length,66);
  assert.deepEqual(JSON.parse(readFileSync(new URL('../public/combined-data.json',import.meta.url))),data);
});
