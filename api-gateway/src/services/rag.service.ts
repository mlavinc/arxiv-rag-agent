import { ragCoreClient } from "../clients/rag-core.client";
import { SearchResponseBody } from "../types/search.types";

async function search(question: string): Promise<SearchResponseBody> {
  return ragCoreClient.search(question);
}

export const ragService = {
  search,
};
