# ArXiv RAG Agent

Sistema RAG para consultar papers científicos de ArXiv mediante preguntas en lenguaje natural.

## Características

- Consultar papers ya indexados
- Agregar nuevos papers
- Obtener respuestas con citas de las fuentes utilizadas

## Arquitectura

```
Frontend (React + TypeScript)
    ↓
API Gateway (Node.js + Express + TypeScript)
    ↓
RAG Core (Python + FastAPI + LangChain)
    ↓
Vector Database (ChromaDB)
    ↓
Embeddings (Ollama - nomic-embed-text)
    ↓
LLM (Ollama - Llama 3)
    ↓
PDFs de ArXiv
```

## Requisitos Previos

- Docker & Docker Compose
- Node.js 18+ (para desarrollo local del frontend y api-gateway)
- Python 3.10+ (para desarrollo local de rag-core)

## Estructura del Proyecto

```
RAG-Agent/
├── frontend/              # React + TypeScript
├── api-gateway/           # Node.js + Express
├── rag-core/              # Python + FastAPI
└── docker-compose.yml     # Orquestación de servicios
```

## Inicio Rápido

### Con Docker Compose (recomendado)

```bash
docker-compose up
```

### Desarrollo Local

Consulta el README de cada servicio:

- [Frontend](./frontend/README.md)
- [API Gateway](./api-gateway/README.md)
- [RAG Core](./rag-core/README.md)

## Sprint Actual

Definición de estructura inicial del proyecto.

## Notas de Arquitectura

- La API Gateway utiliza versionado desde el inicio (`/api/v1/`)
- Cada servicio maneja sus dependencias internamente
- Scripts de desarrollo dentro de cada servicio
- Preparado para despliegue en AWS (API Gateway, Lambda, S3, CloudWatch)
