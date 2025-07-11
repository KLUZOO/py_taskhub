from django.urls import path

from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskTypeListView,
    PositionListView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    toggle_complete_to_task,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "cars/<int:pk>/toggle-complete/",
        toggle_complete_to_task,
        name="toggle-task-complete",
    ),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("accounts/singup/", WorkerCreateView.as_view(), name="singup-create"),
]

app_name = "tasks"
