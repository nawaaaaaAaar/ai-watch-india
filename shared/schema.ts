export type ChangeType = 'Addition' | 'Scope change' | 'Qualification' | 'Wording' | 'Continuity' | 'Timing';
export interface SourceDocument {
  id: string; title: string; instrument: string; documentDate: string;
  publication: string; status: string; url: string; snapshot: string;
  hash: string; hashType: string; description: string; checked: string;
}
export interface Provision {
  familyId?: string; comparisonKind?: string; legalStatus?: string;
  draftUrl?: string; finalUrl?: string; draftLocator?: string; finalLocator?: string;
  beforeLabel?: string; afterLabel?: string; evidenceScope?: string;
  beforeSourceId?: string; afterSourceId?: string; contribution?: boolean;
  id: string; label: string; title: string; draftLabel: string;
  type: ChangeType; actor: string; summary: string; interpretation: string;
  question: string; caution: string; draftText: string; finalText: string;
  correctedText: string; draftPage: number; finalPage: number;
  beforeExcerpt: string; afterExcerpt: string;
  reviewStatus: string; featured: boolean; correctionIds: string[];
}
export interface Correction {
  familyId?: string; sourceUrl?: string;
  id: string; provisionId: string; locator: string; before: string;
  after: string; note: string;
}
export interface Dataset {
  families?: PolicyFamily[];
  title: string; checked: string; sources: SourceDocument[];
  provisions: Provision[]; corrections: Correction[];
}
export interface PolicyFamily {
  id: string; title: string; shortTitle: string; status: string; description: string;
  coverage: string; count: number; contributionCount: number; defaultId: string; scope: string;
  timeline: {date:string;title:string;detail:string}[];
}
export interface Review {
  provisionId: string; reviewer: string; note: string;
  status: 'checked' | 'disputed'; timestamp: string;
}
export interface Notebook {
  version: 1; selected: string[]; reviews: Review[]; title: string;
}
