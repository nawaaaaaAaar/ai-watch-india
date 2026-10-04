export type ChangeType = 'Addition' | 'Scope change' | 'Qualification' | 'Wording' | 'Continuity' | 'Timing';
export interface SourceDocument {
  id: string; title: string; instrument: string; documentDate: string;
  publication: string; status: string; url: string; snapshot: string;
  hash: string; hashType: string; description: string; checked: string;
}
export interface Provision {
  id: string; label: string; title: string; draftLabel: string;
  type: ChangeType; actor: string; summary: string; interpretation: string;
  question: string; caution: string; draftText: string; finalText: string;
  correctedText: string; draftPage: number; finalPage: number;
  beforeExcerpt: string; afterExcerpt: string;
  reviewStatus: string; featured: boolean; correctionIds: string[];
}
export interface Correction {
  id: string; provisionId: string; locator: string; before: string;
  after: string; note: string;
}
export interface Dataset {
  title: string; checked: string; sources: SourceDocument[];
  provisions: Provision[]; corrections: Correction[];
}
export interface Review {
  provisionId: string; reviewer: string; note: string;
  status: 'checked' | 'disputed'; timestamp: string;
}
export interface Notebook {
  version: 1; selected: string[]; reviews: Review[]; title: string;
}
