import axios from "axios";

const API_GATEWAY_URL =
  import.meta.env.VITE_API_GATEWAY_URL ?? "http://localhost:3000";

export const httpClient = axios.create({
  baseURL: API_GATEWAY_URL,
});
