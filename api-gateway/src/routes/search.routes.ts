import { Router } from "express";

import { search } from "../controllers/search.controller";
import { validateBody } from "../middleware/validate.middleware";
import { searchSchema } from "../schemas/search.schema";

const router = Router();

router.post(
  "/api/search",
  validateBody(searchSchema, "question is required"),
  search
);

export default router;
