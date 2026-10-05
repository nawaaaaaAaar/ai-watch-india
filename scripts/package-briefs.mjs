import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { createBrief,mergeCollections } from '../src/lib.mjs';
const data=mergeCollections(JSON.parse(readFileSync(new URL('../src/data/policy.json',import.meta.url))),JSON.parse(readFileSync(new URL('../src/data/expansion.json',import.meta.url))));
const ids=data.provisions.filter(p=>p.contribution).map(p=>p.id);
const dir=new URL('../public/briefs/',import.meta.url);mkdirSync(dir,{recursive:true});
const contents=[];
for(const [index,id] of ids.entries()){
  const p=data.provisions.find(p=>p.id===id);
  const brief=createBrief(data,{version:1,selected:[id],reviews:[],title:`Contribution ${String(index+1).padStart(2,'0')}: ${p.title}`},'5 October 2026');
  writeFileSync(new URL(`${id}.md`,dir),brief);contents.push(brief.replace(/^# /,'## '));
}
writeFileSync(new URL('all-contributions.md',dir),'# AI Watch India: Thirty Policy Research Contributions\n\nThree collections; 18 additional briefs alongside the original 12. These are source-linked desk-research outputs, not exclusive discoveries or legal opinions.\n\n'+contents.join('\n\n---\n\n'));
for(const family of data.families){
  const chosen=ids.map((id,i)=>({p:data.provisions.find(p=>p.id===id),text:contents[i]})).filter(x=>x.p.familyId===family.id);
  writeFileSync(new URL(`${family.id}-contributions.md`,dir),`# AI Watch India: ${family.shortTitle} Contributions\n\n${family.coverage}\n\n`+chosen.map(x=>x.text).join('\n\n---\n\n'));
}
writeFileSync(new URL('../combined-data.json',dir),JSON.stringify(data,null,2)+'\n');
console.log('Packaged 30 contribution briefs, three family bundles and the complete expanded dataset.');
