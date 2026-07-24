import { describe, expect, it } from "vitest";
import request from "supertest";

import app from "../app";

describe("POST /api/search validation", () => {
  it("returns 400 when question is missing", async () => {
    const response = await request(app).post("/api/search").send({});

    expect(response.status).toBe(400);
    expect(response.body).toEqual({ error: "question is required" });
  });

  it("returns 400 when question is an empty string", async () => {
    const response = await request(app)
      .post("/api/search")
      .send({ question: "" });

    expect(response.status).toBe(400);
    expect(response.body).toEqual({ error: "question is required" });
  });
});
