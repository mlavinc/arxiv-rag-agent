# Frontend

Interfaz de usuario del sistema RAG.

## Stack

- React 18
- TypeScript
- (A definir: Vite/Create React App, styling, state management)

## Estructura de Carpetas

```
src/
├── components/      # Componentes reutilizables (UI, formularios, etc.)
├── pages/           # Páginas principales (búsqueda, resultados, gestión)
├── services/        # Cliente HTTP para comunicarse con API Gateway
├── hooks/           # Custom hooks (estado, lógica compartida)
├── types/           # TypeScript types e interfaces
├── utils/           # Funciones auxiliares (formateo, validación, etc.)
└── App.tsx          # Punto de entrada

public/              # Archivos estáticos (favicon, imágenes, etc.)
```

## Responsabilidades

- **components/**: Componentes visuales puros, sin lógica de negocio compleja
- **pages/**: Composición de componentes, manejo de rutas
- **services/**: Abstracción de llamadas HTTP a la API Gateway
- **hooks/**: Lógica reutilizable (custom hooks)
- **types/**: Tipos compartidos que reflejan el contrato de la API
- **utils/**: Funciones puras (formateo, validación, transformación)

## Siguientes Pasos

- [ ] Definir build tool (Vite recomendado)
- [ ] Definir strategy de estado (context API, Redux, Zustand, etc.)
- [ ] Definir styling (Tailwind, CSS Modules, etc.)
- [ ] Crear package.json
