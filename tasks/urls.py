from django.urls import path

from .views import (
    TaskList,
    WorkerList,
    TaskTypeList,
)

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("worker/", WorkerList.as_view(), name="worker_list"),
    path("task-type/", TaskTypeList.as_view(), name="task_type_list"),
]

app_name = "tasks"
