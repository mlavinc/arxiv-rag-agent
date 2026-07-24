import { NextFunction, Request, Response } from "express";
import { ZodType } from "zod";

import { HttpError } from "../utils/http-error";

export function validateBody(schema: ZodType, errorMessage: string) {
  return (req: Request, _res: Response, next: NextFunction): void => {
    const result = schema.safeParse(req.body);

    if (!result.success) {
      next(new HttpError(400, errorMessage));
      return;
    }

    req.body = result.data;
    next();
  };
}
