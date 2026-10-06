"""Synthetic tests only. No file here represents an independent researcher."""
import unittest,tempfile,json,copy,sys,csv
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from compare_coding import agreement,canon,load_ratings,compare,write_csv,FIELDS,ADJ
class AgreementTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
  self.schema={"version":"1.0.0","variables":{"x":{"kind":"nominal","allowed":["A","B","Unknown"]}}}
  self.units=[{"unit_id":"U1","variables":'["x"]',"source_ids":'["D1"]'},{"unit_id":"U2","variables":'["x"]',"source_ids":'["D1"]'}]
  self.expected={("U1","x"),("U2","x")}
  def row(uid,value,coder):return {"schema_version":"1.0.0","unit_id":uid,"variable":"x","reviewer_id":coder,"value":value,"coding_status":"coded","rationale":"Synthetic only","evidence_anchor":"F1","source_access":"synthetic"}
  self.a=[row("U1","A","synthetic_A"),row("U2","B","synthetic_A")]
  self.b=[row("U1","A","synthetic_B"),row("U2","B","synthetic_B")]
 def tearDown(self):self.tmp.cleanup()
 def load(self,rows,name="ratings.csv",partial=False):
  path=self.root/name;write_csv(path,rows,FIELDS);return load_ratings(path,self.schema,self.expected,partial)
 def test_known_kappa_table(self):
  m=agreement([("A","A")]*42+[("A","B")]*8+[("B","A")]*13+[("B","B")]*37,"nominal")
  self.assertAlmostEqual(m["observed_agreement"],.79);self.assertAlmostEqual(m["kappa"],.58)
 def test_perfect_variable_agreement(self):self.assertEqual(agreement([("A","A"),("B","B")],"nominal")["kappa"],1)
 def test_constant_category_is_undefined(self):
  m=agreement([("Unknown","Unknown")]*3,"nominal");self.assertIsNone(m["kappa"]);self.assertEqual(m["observed_agreement"],1)
 def test_zero_pairs_is_not_perfect(self):
  m=agreement([],"nominal");self.assertIsNone(m["kappa"]);self.assertIsNone(m["observed_agreement"])
 def test_negative_kappa(self):self.assertEqual(agreement([("A","B"),("B","A")],"nominal")["kappa"],-1)
 def test_set_equality_is_order_independent(self):
  spec={"kind":"set","allowed":["Estimate","Bid security","Not established"]}
  a=canon('["Estimate","Bid security"]',spec);b=canon('["Bid security","Estimate"]',spec)
  self.assertEqual(agreement([(a,b)],"set")["observed_agreement"],1)
 def test_set_jaccard_is_not_nominal_kappa(self):
  m=agreement([('["Estimate","Bid security"]','["Estimate"]')],"set")
  self.assertEqual(m["mean_jaccard"],.5);self.assertIsNone(m["kappa"])
 def test_unknown_set_cannot_mix(self):
  with self.assertRaises(ValueError):canon('["Not established","Estimate"]',{"kind":"set","allowed":["Not established","Estimate"]})
 def test_duplicate_or_unknown_key_rejected(self):
  for rows in [self.b+[self.b[0]],[dict(self.b[0],unit_id="invalid"),self.b[1]]]:
   with self.assertRaises(ValueError):self.load(rows)
 def test_missing_rows_require_partial_mode(self):
  with self.assertRaises(ValueError):self.load(self.b[:1])
  self.assertEqual(len(self.load(self.b[:1],partial=True)),1)
 def test_invalid_label_rejected(self):
  with self.assertRaises(ValueError):self.load([dict(self.b[0],value="invented"),self.b[1]])
 def test_version_mismatch_rejected(self):
  with self.assertRaises(ValueError):self.load([dict(self.b[0],schema_version="2.0"),self.b[1]])
 def test_coded_rationale_is_required(self):
  with self.assertRaises(ValueError):self.load([dict(self.b[0],rationale=""),self.b[1]])
 def test_mixed_coder_submission_rejected(self):
  with self.assertRaises(ValueError):self.load([dict(self.b[0],reviewer_id="another"),self.b[1]])
 def test_uncoded_value_cannot_fake_unknown(self):
  with self.assertRaises(ValueError):self.load([dict(self.b[0],coding_status="unresolved",value="Unknown"),self.b[1]])
 def test_substantive_unknown_is_scored(self):
  a=self.load([dict(self.a[0],value="Unknown"),self.a[1]],"a.csv")
  b=self.load([dict(self.b[0],value="Unknown"),self.b[1]],"b.csv")
  self.assertEqual(compare(a,b,self.schema,self.units,self.root/"out")["paired_ratings"],2)
 def test_unresolved_is_excluded_and_counted(self):
  a=self.load(self.a,"a.csv");b=self.load([dict(self.b[0],coding_status="unresolved",value=""),self.b[1]],"b.csv")
  s=compare(a,b,self.schema,self.units,self.root/"out");self.assertEqual(s["paired_ratings"],1);self.assertEqual(s["unpaired_rows"],1)
 def test_template_waits_for_review(self):
  a=self.load(self.a,"a.csv");b=self.load([dict(r,reviewer_id="",value="",coding_status="pending",rationale="",evidence_anchor="",source_access="") for r in self.b],"b.csv")
  s=compare(a,b,self.schema,self.units,self.root/"out");self.assertEqual(s["state"],"waiting_for_second_review");self.assertEqual(s["paired_ratings"],0)
 def test_same_coder_pass_is_not_an_independent_comparison(self):
  a=self.load(self.a,"a.csv")
  with self.assertRaises(ValueError):compare(a,a,self.schema,self.units,self.root/"out")
 def test_shared_source_observations_count_once(self):
  s=compare(self.load(self.a,"a.csv"),self.load(self.b,"b.csv"),self.schema,self.units,self.root/"out")
  self.assertEqual(s["assigned_ratings"],2);self.assertEqual(s["metrics"]["x"]["paired"],2)
 def test_adjudication_keeps_raw_disagreement(self):
  a=self.load(self.a,"a.csv");b=self.load([dict(self.b[0],value="B"),self.b[1]],"b.csv")
  decision={k:"" for k in ADJ};decision.update(unit_id="U1",variable="x",reference_value="A",review_value="B",decision="resolved",resolved_value="B",cause="interpretation",rationale="Synthetic source review",evidence_anchor="F1",adjudicator="synthetic_C",reference_ack="acknowledged",review_ack="acknowledged",decision_date="2026-10-06")
  p=self.root/"completed.csv";write_csv(p,[decision],ADJ)
  s=compare(a,b,self.schema,self.units,self.root/"out",p)
  self.assertEqual(s["disagreement_rows"],1);self.assertEqual(s["metrics"]["x"]["observed_agreement"],.5);self.assertEqual(a[("U1","x")]["value"],"A")
  self.assertTrue((self.root/"out/consensus.csv").exists())
 def test_invalid_consensus_is_rejected(self):
  a=self.load(self.a,"a.csv");b=self.load([dict(self.b[0],value="B"),self.b[1]],"b.csv")
  decision={k:"" for k in ADJ};decision.update(unit_id="U1",variable="x",reference_value="A",review_value="B",decision="resolved",resolved_value="invented",cause="format",rationale="Synthetic",evidence_anchor="F1",adjudicator="C",reference_ack="acknowledged",review_ack="acknowledged",decision_date="2026-10-06")
  p=self.root/"completed.csv";write_csv(p,[decision],ADJ)
  with self.assertRaises(ValueError):compare(a,b,self.schema,self.units,self.root/"out",p)
 def test_initial_values_in_adjudication_cannot_change(self):
  a=self.load(self.a,"a.csv");b=self.load([dict(self.b[0],value="B"),self.b[1]],"b.csv")
  decision={k:"" for k in ADJ};decision.update(unit_id="U1",variable="x",reference_value="Unknown",review_value="B",decision="unresolved")
  p=self.root/"completed.csv";write_csv(p,[decision],ADJ)
  with self.assertRaises(ValueError):compare(a,b,self.schema,self.units,self.root/"out",p)
 def test_non_equivalent_construct_does_not_get_reliability_kappa(self):
  self.schema["variables"]["x"]["comparable_reference"]=False
  s=compare(self.load(self.a,"a.csv"),self.load(self.b,"b.csv"),self.schema,self.units,self.root/"out")
  self.assertIsNone(s["metrics"]["x"]["kappa"]);self.assertEqual(s["diagnostic_paired_ratings"],2);self.assertEqual(s["comparable_paired_ratings"],0)
if __name__=="__main__":unittest.main()
