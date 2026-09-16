#!/usr/bin/env bash
set -euo pipefail
set -a; source .env; set +a

kubectl create secret generic airflow-connections -n airflow \
  --from-literal=AIRFLOW_CONN_MINIO_S3="$AIRFLOW_CONN_MINIO_S3" \
  --dry-run=client -o yaml | kubectl apply -f -

kubectl create secret generic minio-root -n minio \
  --from-literal=MINIO_ROOT_USER="$MINIO_ROOT_USER" \
  --from-literal=MINIO_ROOT_PASSWORD="$MINIO_ROOT_PASSWORD" \
  --dry-run=client -o yaml | kubectl apply -f -