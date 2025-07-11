from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from tasks.forms import WorkerCreationForm, TaskForm
from tasks.models import Task, Worker, TaskType, Position


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.select_related("task_type").prefetch_related("assignees").all().ordered_by_priority()
    template_name = "tasks/index.html"

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["num_tasks"] = Task.objects.count()
        context["num_workers"] = Worker.objects.count()
        context["num_positions"] = Position.objects.count()
        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1
        context["num_visits"] = num_visits
        return context


class TaskDetailView(generic.DetailView):
    model = Task


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


@login_required
def toggle_complete_to_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.user in task.assignees.all():
        if task.is_complete:
            task.is_complete = False
            task.save()
        else:
            task.is_complete = True
            task.save()
    return HttpResponseRedirect(reverse_lazy("tasks:task-detail", args=[pk]))
