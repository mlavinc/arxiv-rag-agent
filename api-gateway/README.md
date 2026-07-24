# API Gateway

Este servicio es el **API Gateway** del proyecto ArXiv RAG Agent. Es el punto de entrada para clientes externos (frontend, herramientas, etc.) y se encarga de comunicar esas peticiones con el **RAG Core** (servicio Python + FastAPI), donde vive toda la lógica de RAG (embeddings, ChromaDB, LLM).

```
Usuario
  ↓
API Gateway (Node.js + TypeScript + Express)
  ↓
RAG Core (FastAPI)
  ↓
ChromaDB + Ollama
```

**Importante:** este servicio **no contiene lógica de RAG**. Solo valida, orquesta y reenvía solicitudes hacia el RAG Core. Toda la inteligencia (retrieval, embeddings, generación) permanece en Python.

## Stack

- Node.js
- TypeScript (strict mode)
- Express 5
- axios (cliente HTTP hacia RAG Core)
- Zod (validación de requests)
- Helmet (headers de seguridad)
- CORS
- Vitest + Supertest (tests)

## Estructura de Carpetas

```
src/
├── index.ts               # Punto de entrada: arranca el servidor HTTP
├── app.ts                 # Configuración de la app Express (middleware, routers)
├── routes/                 # Definición de rutas Express
├── controllers/            # Reciben el request, delegan a services
├── services/                # Orquestación de la comunicación con RAG Core
├── clients/                 # Cliente HTTP hacia el servicio RAG Core (FastAPI)
├── config/                  # Configuración y variables de entorno
├── types/                   # Tipos e interfaces de TypeScript
├── schemas/                 # Schemas de validación (Zod)
├── middleware/               # Middleware (errores, logging, validación)
├── utils/                    # Utilidades (ej. HttpError)
└── __tests__/                 # Tests (Vitest + Supertest)
```

## Variables de entorno

Ver `.env.example`:

- `PORT` — puerto del servidor (default `3000`)
- `RAG_CORE_URL` — URL base del RAG Core (default `http://localhost:8000`)
- `CORS_ORIGIN` — origen permitido por CORS (default `http://localhost:5173`, para desarrollo local del frontend)

## Cómo ejecutar

```bash
npm install

# Desarrollo (con recarga automática)
npm run dev

# Compilar
npm run build

# Ejecutar versión compilada
npm start

# Correr tests
npm test
```

## Endpoints disponibles

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/health` | Estado del servicio (`{"status":"ok","service":"api-gateway"}`) |
| `POST` | `/api/search` | Recibe `{"question": "..."}`, valida y reenvía a `POST {RAG_CORE_URL}/api/v1/search` |

### Errores

Formato consistente: `{"error": "mensaje"}`

| Código | Caso |
|---|---|
| `400` | `question` ausente, vacío o no es string |
| `503` | RAG Core no responde |
| `500` | Error inesperado |

## Estado actual

Sprint 6 completo: bootstrap, proxy hacia RAG Core, manejo de errores centralizado, validación con Zod, CORS, Helmet, logging básico y tests. Sin autenticación ni lógica de negocio (permanece en RAG Core).
