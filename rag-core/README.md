# RAG Core

Núcleo inteligente del sistema. Orquestación RAG, embeddings, búsqueda vectorial y LLM.

## Stack

- Python 3.10+
- FastAPI
- LangChain
- ChromaDB
- Ollama

## Estructura de Carpetas

```
app/
├── api/
│   └── endpoints/       # Rutas FastAPI (/api/v1/...)
├── core/
│   ├── config.py        # Configuración global (env, constantes)
│   └── constants.py     # Constantes del dominio
├── services/
│   ├── embeddings/      # Servicio de embeddings (Ollama - nomic-embed-text)
│   ├── vector_db/       # Servicio de ChromaDB (almacenamiento vectorial)
│   ├── llm/             # Servicio de LLM (Ollama - Llama 3)
│   └── rag/             # Orquestación de RAG (búsqueda + generación)
├── schemas/             # Pydantic models (DTOs, validación)
├── utils/               # Funciones auxiliares
├── dependencies.py      # Inyección de dependencias FastAPI
└── main.py              # Punto de entrada, configuración de app

tests/                   # Tests unitarios e integración
```

## Responsabilidades

- **api/endpoints/**: Definir endpoints `/api/v1/...` que expongan la funcionalidad RAG
- **core/**: Configuración centralizada
- **services/embeddings/**: Abstracción de Ollama para generar embeddings
- **services/vector_db/**: Abstracción de ChromaDB (CRUD de documents y búsqueda)
- **services/llm/**: Abstracción de Ollama LLM para generación de respuestas
- **services/rag/**: Orquestación del flujo completo (retrieval + generation)
- **schemas/**: Validación de inputs/outputs usando Pydantic
- **utils/**: Funciones auxiliares (parseo de PDFs, logging, etc.)
- **dependencies.py**: Dependency injection FastAPI (inyectar services en endpoints)

## Flujo RAG

1. Usuario hace pregunta vía API Gateway
2. RAG Core recibe pregunta
3. Embeddings Service: convierte pregunta a vector
4. Vector DB Service: busca documentos similares (similarity search)
5. LLM Service: genera respuesta usando documents + prompt
6. Response retorna al usuario con citations

## Siguientes Pasos

- [ ] Crear requirements.txt
- [ ] Configurar FastAPI app
- [ ] Crear .env.example
- [ ] Crear Dockerfile
