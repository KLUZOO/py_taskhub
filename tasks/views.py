from django.shortcuts import render
from django.views import generic

from tasks.models import Task, Worker


class TaskList(generic.ListView):
    model = Task
    fields = "__all__"
    template_name = "tasks/index.html"

class WorkerList(generic.ListView):
    model = Worker
    fields = "__all__"
    template_name = "tasks/worker_list.html"