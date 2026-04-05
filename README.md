# SocialMedia Insights SaaS (Monorepo)

Plataforma SaaS B2B para análisis de contenido de TikTok, YouTube Shorts, Instagram Reels y Facebook videos, con recomendaciones y predicciones asistidas por IA (Vertex AI Gemini).

## Stack

- **Frontend:** Next.js 15 + TypeScript + Tailwind
- **Backend:** FastAPI + Python 3.11
- **IA:** Vertex AI Gemini
- **DB/Auth:** Supabase PostgreSQL + Supabase Auth
- **Infra:** Docker + Google Cloud Run
- **CI/CD:** GitHub Actions
- **Monorepo:** `apps/web` + `apps/api`

## Estructura

```bash
.
├── apps/
│   ├── api/
│   └── web/
├── infra/
│   └── terraform/
├── .github/workflows/
├── docker-compose.yml
├── cloudbuild.yaml
└── deploy.sh
```

## Requisitos

- Node.js 20+
- Python 3.11+
- Docker + Docker Compose
- gcloud CLI autenticado
- Proyecto de GCP con Vertex AI habilitado
- Proyecto de Supabase

## Variables de entorno

1. Copia `apps/api/.env.example` a `apps/api/.env`.
2. Copia `apps/web/.env.example` a `apps/web/.env.local`.

## Desarrollo local

```bash
# En la raíz
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Docs OpenAPI: http://localhost:8000/docs

## Testing

```bash
# API
cd apps/api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Deploy a Cloud Run

### Opción A: script

```bash
chmod +x deploy.sh
./deploy.sh
```

### Opción B: Cloud Build

```bash
gcloud builds submit --config cloudbuild.yaml
```

## Terraform (opcional)

En `infra/terraform` se incluye un módulo base para servicios de Cloud Run + cuentas de servicio.

```bash
cd infra/terraform
terraform init
terraform plan -var="project_id=<tu-project-id>"
terraform apply -var="project_id=<tu-project-id>"
```

## Arquitectura backend

- `routes/`: endpoints REST
- `schemas/`: contratos Pydantic
- `services/`: lógica de negocio + IA
- `repositories/`: acceso a datos (Supabase)
- `core/`: config, logging, seguridad, rate limiting, errores

## Seguridad y buenas prácticas

- Autenticación JWT validada con Supabase
- Rate limiting por IP/usuario
- Logging estructurado JSON
- Manejo centralizado de errores
- Diseño multi-tenant por `workspace_id`

## Endpoints IA

- `POST /api/v1/ai/analyze-video`
- `POST /api/v1/ai/generate-script`
- `POST /api/v1/ai/predict-growth`

## Exportaciones

- `GET /api/v1/export/videos.csv`
- `GET /api/v1/export/report.pdf` (placeholder, listo para integrar motor PDF)

