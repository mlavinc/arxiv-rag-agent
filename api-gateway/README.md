# API Gateway

Puerta de entrada de la aplicación. Orquestación, validación y enrutamiento de requests.

## Stack

- Node.js 18+
- Express
- TypeScript

## Estructura de Carpetas

```
src/
├── routes/          # Definición de rutas Express (/api/v1/...)
├── middleware/      # Middleware (error handling, logging, CORS, etc.)
├── controllers/     # Orquestación de requests, llamadas a services
├── services/        # Clientes HTTP para comunicarse con RAG Core
├── types/           # TypeScript types e interfaces
├── config/          # Configuración (variables de entorno, constantes)
├── utils/           # Funciones auxiliares
└── main.ts          # Punto de entrada
```

## Responsabilidades

- **routes/**: Definir endpoints `/api/v1/...` (búsqueda, ingesta, etc.)
- **middleware/**: Error handling, validación de inputs, logging, CORS
- **controllers/**: Recibir request, validar datos, llamar services
- **services/**: Abstracción para comunicarse con RAG Core (cliente HTTP)
- **types/**: Interfaces de request/response
- **config/**: Variables de entorno, puertos, URLs base del RAG Core
- **utils/**: Funciones auxiliares (serialización, transformación)

## Patrón Arquitectónico

Este es un **API Gateway tipo "thin"**:
- Valida inputs
- Orquesta llamadas a servicios
- Maneja errores
- NO contiene lógica de negocio pesada (esa es responsabilidad de RAG Core)

## Versioning de API

Todos los endpoints respetan `/api/v1/...` para permitir versionado futuro.

## Siguientes Pasos

- [ ] Crear package.json
- [ ] Configurar TypeScript
- [ ] Crear .env.example
- [ ] Definir estructura de error handling
