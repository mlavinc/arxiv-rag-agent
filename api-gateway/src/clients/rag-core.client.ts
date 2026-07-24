import axios from "axios";

import { env } from "../config/env";
import { SearchResponseBody } from "../types/search.types";

const httpClient = axios.create({
  baseURL: env.RAG_CORE_URL,
});

async function search(question: string): Promise<SearchResponseBody> {
  const response = await httpClient.post<SearchResponseBody>(
    "/api/v1/search",
    { question }
  );

  return response.data;
}

export const ragCoreClient = {
  search,
};
