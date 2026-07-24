import axios from "axios";
import FormData from "form-data";

import { env } from "../config/env";
import { DocumentIngestResponseBody } from "../types/documents.types";
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

async function ingestDocument(
  file: Express.Multer.File
): Promise<DocumentIngestResponseBody> {
  const formData = new FormData();
  formData.append("file", file.buffer, {
    filename: file.originalname,
    contentType: file.mimetype,
  });

  const response = await httpClient.post<DocumentIngestResponseBody>(
    "/api/v1/documents/ingest",
    formData,
    { headers: formData.getHeaders() }
  );

  return response.data;
}

export const ragCoreClient = {
  search,
  ingestDocument,
};
