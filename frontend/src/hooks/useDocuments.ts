import axios from "axios";
import { useCallback, useState } from "react";

import { ingestDocument } from "../api/documents.client";
import { IngestedDocument } from "../types/rag.types";

interface UseDocumentsResult {
  documents: IngestedDocument[];
  isUploading: boolean;
  error: string | null;
  uploadDocument: (file: File) => Promise<void>;
}

export function useDocuments(): UseDocumentsResult {
  const [documents, setDocuments] = useState<IngestedDocument[]>([]);
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const uploadDocument = useCallback(async (file: File) => {
    setIsUploading(true);
    setError(null);

    try {
      const result = await ingestDocument(file);

      setDocuments((previous) => [
        {
          filename: result.filename,
          chunks: result.chunks,
          status: result.status,
          ingestedAt: new Date().toISOString(),
        },
        ...previous,
      ]);
    } catch (uploadError) {
      const message = axios.isAxiosError(uploadError)
        ? uploadError.response?.data?.error ?? "Could not process the document."
        : "Could not process the document.";

      setError(message);
    } finally {
      setIsUploading(false);
    }
  }, []);

  return { documents, isUploading, error, uploadDocument };
}
