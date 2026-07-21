# Docker Compose Configuration

Orquestación de servicios para desarrollo local.

## Servicios

- **frontend**: React app (puerto 3000)
- **api-gateway**: Express API (puerto 3001)
- **rag-core**: FastAPI (puerto 8000)
- **ollama**: LLM + Embeddings (puerto 11434)
- **chromadb**: Vector Database (puerto 8001)

## Uso

```bash
# Iniciar todos los servicios
docker-compose up

# Iniciar en background
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar servicios
docker-compose down
```

## Notas de Desarrollo

- Los servicios se comunican por el nombre del servicio (ej: http://rag-core:8000)
- Los puertos están expuestos al host para desarrollo local
- Volúmenes compartidos para código fuente (hot reload)
- `.env` se carga automáticamente

## Siguientes Pasos

- [ ] Crear Dockerfile para cada servicio
- [ ] Configurar docker-compose.yml con servicios
- [ ] Definir healthchecks
