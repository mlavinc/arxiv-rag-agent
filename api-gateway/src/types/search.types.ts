export interface SearchRequestBody {
  question: string;
}

export interface SearchSource {
  document_id: string;
  title: string;
  chunk_index: number;
  score: number;
}

export interface SearchResponseBody {
  answer: string;
  sources: SearchSource[];
}
