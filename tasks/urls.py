from django.urls import path

from .views import (
    TaskList,
    WorkerList,
)

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("worker/", WorkerList.as_view(), name="worker_list"),
]

app_name = "tasks"
