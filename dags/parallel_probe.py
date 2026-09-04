from __future__ import annotations

import os
import time
from datetime import datetime

import pendulum
from airflow.sdk import dag, task


@dag(
    dag_id="parallel_probe",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["gitsync"],
)
def parallel_probe():
    @task
    def sleeper(n: int) -> str:
        started = datetime.now().isoformat(timespec="seconds")
        time.sleep(30)
        return f"n={n} pid={os.getpid()} started={started}"

    sleeper.expand(n=list(range(8)))


parallel_probe()