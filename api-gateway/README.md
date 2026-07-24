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
- Express
- axios (cliente HTTP hacia RAG Core)

## Estructura de Carpetas

```
src/
├── index.ts             # Punto de entrada: arranca el servidor HTTP
├── app.ts               # Configuración de la app Express (middleware, routers)
├── routes/               # Definición de rutas Express
├── controllers/          # Reciben el request, delegan a services
├── services/              # Orquestación de la comunicación con RAG Core
├── clients/               # Cliente HTTP hacia el servicio RAG Core (FastAPI)
├── config/                # Configuración y variables de entorno
└── types/                 # Tipos e interfaces de TypeScript
```

## Scripts

- `npm run dev` — levanta el servidor en modo desarrollo con recarga automática
- `npm run build` — compila TypeScript a JavaScript (`dist/`)
- `npm start` — ejecuta la versión compilada

## Estado actual

Sprint 6.1: solo estructura base creada. Sin lógica de negocio ni endpoints implementados todavía.
