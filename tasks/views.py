from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from tasks.forms import WorkerCreationForm, TaskForm
from tasks.models import Task, Worker, TaskType, Position


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"
    template_name = "tasks/index.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")
    template_name = "tasks/task_form.html"


class WorkerListView(generic.ListView):
    model = Worker
    fields = "__all__"
    template_name = "tasks/worker_list.html"


class WorkerCreateView(generic.CreateView):
    model = Worker
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    form_class = WorkerCreationForm


class TaskTypeListView(generic.ListView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_list.html"


class PositionListView(generic.ListView):
    model = Position
    fields = "__all__"
    template_name = "tasks/position_list.html"
