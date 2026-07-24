import { Router } from "express";

import { ingestDocument } from "../controllers/documents.controller";
import { uploadPdf } from "../middleware/upload.middleware";

const router = Router();

router.post("/api/documents/ingest", uploadPdf, ingestDocument);

export default router;
