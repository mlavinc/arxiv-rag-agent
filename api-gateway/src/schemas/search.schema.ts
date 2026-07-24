import { z } from "zod";

export const searchSchema = z.object({
  question: z.string().min(1),
});
