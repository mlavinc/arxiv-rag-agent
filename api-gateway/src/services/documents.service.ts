import { ragCoreClient } from "../clients/rag-core.client";
import { DocumentIngestResponseBody } from "../types/documents.types";

async function ingest(
  file: Express.Multer.File
): Promise<DocumentIngestResponseBody> {
  return ragCoreClient.ingestDocument(file);
}

export const documentsService = {
  ingest,
};
