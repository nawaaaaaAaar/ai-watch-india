import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
test('AI Watch brand keeps India as explicit research scope',()=>{
  const app=readFileSync(new URL('../src/main.tsx',import.meta.url),'utf8');
  const html=readFileSync(new URL('../index.html',import.meta.url),'utf8');
  assert.ok(app.includes('<b>AI Watch</b><small>INDIA EVIDENCE DESK</small>'));
  assert.ok(app.includes('aria-label="AI Watch mark"'));
  assert.ok(html.includes('<title>AI Watch · India evidence desk</title>'));
  assert.ok(html.includes('https://fonts.googleapis.com'));
});
