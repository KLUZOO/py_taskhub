from django.shortcuts import render
from django.views import generic

from tasks.models import Task, Worker, TaskType, Position


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"
    template_name = "tasks/index.html"


class WorkerListView(generic.ListView):
    model = Worker
    fields = "__all__"
    template_name = "tasks/worker_list.html"


class TaskTypeListView(generic.ListView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_list.html"

class PositionListView(generic.ListView):
    model = Position
    fields = "__all__"
    template_name = "tasks/position_list.html"


class WorkerCreateView(generic.CreateView):
    model = Worker
    template_name = "registration/signup.html"
    fields = "__all__"
