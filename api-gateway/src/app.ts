import express from "express";

import healthRoutes from "./routes/health.routes";
import searchRoutes from "./routes/search.routes";

const app = express();

app.use(express.json());

app.use(healthRoutes);
app.use(searchRoutes);

export default app;
