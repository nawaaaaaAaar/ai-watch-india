import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { createBrief } from '../src/lib.mjs';
const data=JSON.parse(readFileSync(new URL('../src/data/policy.json',import.meta.url)));
const ids=['rule-8','rule-14','rule-13','schedule-fourth','rule-7','rule-11','schedule-second','rule-1','rule-6','rule-3','rule-15','rule-23'];
const dir=new URL('../public/briefs/',import.meta.url);mkdirSync(dir,{recursive:true});
const contents=[];
for(const [index,id] of ids.entries()){
  const p=data.provisions.find(p=>p.id===id);
  const brief=createBrief(data,{version:1,selected:[id],reviews:[],title:`Contribution ${String(index+1).padStart(2,'0')}: ${p.title}`},'4 October 2026');
  writeFileSync(new URL(`${id}.md`,dir),brief);contents.push(brief.replace(/^# /,'## '));
}
writeFileSync(new URL('all-contributions.md',dir),'# AI Watch India: Twelve Policy Research Contributions\n\nEach contribution is a source-linked desk-research brief, not an exclusive discovery or legal opinion.\n\n'+contents.join('\n\n---\n\n'));
console.log('Packaged 12 distinct contribution briefs and the complete bundle.');
