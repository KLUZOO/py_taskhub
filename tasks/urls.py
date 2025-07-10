from django.urls import path

from .views import (
    TaskListView,
    WorkerListView,
    TaskTypeListView,
    PositionListView,
    WorkerCreateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("worker/", WorkerListView.as_view(), name="worker_list"),
    path("task-type/", TaskTypeListView.as_view(), name="task_type_list"),
    path("position/", PositionListView.as_view(), name="position_list"),
    path("accounts/singup/", WorkerCreateView.as_view(), name="singup_create"),
]

app_name = "tasks"
