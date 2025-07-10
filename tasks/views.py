from django.shortcuts import render
from django.views import generic

from tasks.models import Task, Worker, TaskType, Position


class TaskList(generic.ListView):
    model = Task
    fields = "__all__"
    template_name = "tasks/index.html"


class WorkerList(generic.ListView):
    model = Worker
    fields = "__all__"
    template_name = "tasks/worker_list.html"


class TaskTypeList(generic.ListView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_list.html"

class PositionList(generic.ListView):
    model = Position
    fields = "__all__"
    template_name = "tasks/position_list.html"
