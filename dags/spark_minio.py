from datetime import datetime

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import (
    SparkKubernetesOperator,
)

with DAG(
    dag_id="spark_minio",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["spark"],
) as dag:
    submit = SparkKubernetesOperator(
        task_id="submit_spark_job",
        namespace="spark",
        application_file="minio_probe_app.yaml",
        kubernetes_conn_id="kubernetes_default",
        get_logs=True,
        delete_on_termination=False,
    )