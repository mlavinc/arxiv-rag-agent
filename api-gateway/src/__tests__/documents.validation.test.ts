import { describe, expect, it } from "vitest";
import request from "supertest";

import app from "../app";

describe("POST /api/documents/ingest validation", () => {
  it("returns 400 when no file is provided", async () => {
    const response = await request(app).post("/api/documents/ingest");

    expect(response.status).toBe(400);
    expect(response.body).toEqual({ error: "file is required" });
  });

  it("returns 400 when the uploaded file is not a PDF", async () => {
    const response = await request(app)
      .post("/api/documents/ingest")
      .attach("file", Buffer.from("plain text content"), {
        filename: "notes.txt",
        contentType: "text/plain",
      });

    expect(response.status).toBe(400);
    expect(response.body).toEqual({ error: "Only PDF files are allowed" });
  });
});
