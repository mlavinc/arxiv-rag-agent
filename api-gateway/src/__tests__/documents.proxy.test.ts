import { beforeEach, describe, expect, it, vi } from "vitest";
import request from "supertest";

const { mockPost } = vi.hoisted(() => ({
  mockPost: vi.fn(),
}));

vi.mock("axios", () => ({
  default: {
    create: vi.fn(() => ({ post: mockPost })),
  },
}));

import app from "../app";

describe("POST /api/documents/ingest proxy", () => {
  beforeEach(() => {
    mockPost.mockReset();
  });

  it("forwards the uploaded PDF internally to RAG Core's POST /api/v1/documents/ingest", async () => {
    mockPost.mockResolvedValue({
      data: { filename: "paper.pdf", chunks: 3, status: "completed" },
    });

    const response = await request(app)
      .post("/api/documents/ingest")
      .attach("file", Buffer.from("%PDF-1.4 mock content"), {
        filename: "paper.pdf",
        contentType: "application/pdf",
      });

    expect(mockPost).toHaveBeenCalledWith(
      "/api/v1/documents/ingest",
      expect.anything(),
      expect.objectContaining({ headers: expect.any(Object) })
    );
    expect(response.status).toBe(200);
    expect(response.body).toEqual({
      filename: "paper.pdf",
      chunks: 3,
      status: "completed",
    });
  });

  it("returns 503 when RAG Core is unreachable", async () => {
    mockPost.mockRejectedValue(new Error("connection refused"));

    const response = await request(app)
      .post("/api/documents/ingest")
      .attach("file", Buffer.from("%PDF-1.4 mock content"), {
        filename: "paper.pdf",
        contentType: "application/pdf",
      });

    expect(response.status).toBe(503);
    expect(response.body).toEqual({ error: "RAG Core unavailable" });
  });
});
