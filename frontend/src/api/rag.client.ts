import { httpClient } from "./http";
import { SearchResponseBody } from "../types/rag.types";

export async function askQuestion(
  question: string
): Promise<SearchResponseBody> {
  const response = await httpClient.post<SearchResponseBody>("/api/search", {
    question,
  });

  return response.data;
}
