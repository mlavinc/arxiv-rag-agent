import { Request, Response } from "express";

import { ragService } from "../services/rag.service";
import { SearchRequestBody } from "../types/search.types";

export async function search(
  req: Request<unknown, unknown, Partial<SearchRequestBody>>,
  res: Response
): Promise<void> {
  const { question } = req.body;

  if (!question) {
    res.status(400).json({ error: "question is required" });
    return;
  }

  try {
    const result = await ragService.search(question);
    res.json(result);
  } catch (error) {
    res.status(503).json({ error: "RAG Core unavailable" });
  }
}
