from django.shortcuts import render
from django.views import generic

from tasks.models import Task


class TaskList(generic.ListView):
    model = Task
    fields = "__all__"
    template_name = "tasks/index.html"