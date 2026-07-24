import cors from "cors";
import express from "express";
import helmet from "helmet";

import { env } from "./config/env";
import { errorMiddleware } from "./middleware/error.middleware";
import { requestLogger } from "./middleware/logger.middleware";
import documentsRoutes from "./routes/documents.routes";
import healthRoutes from "./routes/health.routes";
import searchRoutes from "./routes/search.routes";

const app = express();

app.use(helmet());
app.use(cors({ origin: env.CORS_ORIGIN }));
app.use(express.json());
app.use(requestLogger);

app.use(healthRoutes);
app.use(searchRoutes);
app.use(documentsRoutes);

app.use(errorMiddleware);

export default app;
