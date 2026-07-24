import dotenv from "dotenv";

dotenv.config();

export const env = {
  PORT: Number(process.env.PORT) || 3000,
  RAG_CORE_URL: process.env.RAG_CORE_URL || "http://localhost:8000",
  CORS_ORIGIN: process.env.CORS_ORIGIN || "http://localhost:5173",
};
