from __future__ import annotations
import pendulum
from airflow.sdk import dag, task
from kubernetes.client import models as k8s


def pod_with_memory(mem: str, cpu: str = "100m"):
    return {
        "pod_override": k8s.V1Pod(
            spec=k8s.V1PodSpec(
                containers=[
                    k8s.V1Container(
                        name="base",
                        resources=k8s.V1ResourceRequirements(
                            requests={"memory": mem, "cpu": cpu},
                        ),
                    )
                ]
            )
        )
    }


@dag(
    dag_id="resource_probe",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["phase1"],
)
def resource_probe():
    @task
    def small() -> str:
        return "default resources"

    @task(executor_config=pod_with_memory("1Gi", "500m"))
    def large() -> str:
        return "overridden resources"

    @task(executor_config=pod_with_memory("24Gi"))
    def impossible() -> str:
        return "never runs"

    small()
    large()
    impossible()


resource_probe()
