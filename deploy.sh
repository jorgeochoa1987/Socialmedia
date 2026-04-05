#!/usr/bin/env bash
set -euo pipefail

PROJECT_ID="${GCP_PROJECT_ID:-}"
REGION="${GCP_REGION:-us-central1}"

if [[ -z "${PROJECT_ID}" ]]; then
  echo "GCP_PROJECT_ID is required"
  exit 1
fi

API_SERVICE="socialmedia-api"
WEB_SERVICE="socialmedia-web"

# Build and push images using Cloud Build

gcloud builds submit ./apps/api --tag "gcr.io/${PROJECT_ID}/${API_SERVICE}:latest"
gcloud builds submit ./apps/web --tag "gcr.io/${PROJECT_ID}/${WEB_SERVICE}:latest"

# Deploy API

gcloud run deploy "${API_SERVICE}" \
  --image "gcr.io/${PROJECT_ID}/${API_SERVICE}:latest" \
  --platform managed \
  --region "${REGION}" \
  --allow-unauthenticated

# Deploy Web

gcloud run deploy "${WEB_SERVICE}" \
  --image "gcr.io/${PROJECT_ID}/${WEB_SERVICE}:latest" \
  --platform managed \
  --region "${REGION}" \
  --allow-unauthenticated

echo "Deploy completed"
