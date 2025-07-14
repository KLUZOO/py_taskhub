from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from tasks.forms import WorkerCreationForm, TaskForm, TaskCreateForm, WorkerUpdateForm, SearchForm
from tasks.models import Task, Worker, TaskType, Position


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["num_tasks"] = Task.objects.count()
        context["num_workers"] = Worker.objects.count()
        context["num_positions"] = Position.objects.count()
        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1
        context["num_visits"] = num_visits
        title = self.request.GET.get("title", "")
        context["search"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return Task.objects.filter(
                Q(name__icontains=form.cleaned_data["title"]) |
                Q(description__icontains=form.cleaned_data["title"])
            ).select_related("task_type").prefetch_related("assignees").ordered_by_priority()
        return Task.objects.select_related("task_type").prefetch_related("assignees").all().ordered_by_priority()


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")
    template_name = "tasks/task_form.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.prefetch_related("tasks").all()


class WorkerListView(generic.ListView):
    model = Worker
    fields = "__all__"
    template_name = "tasks/worker_list.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return Worker.objects.filter(
                Q(username__icontains=form.cleaned_data["title"]) |
                Q(first_name__icontains=form.cleaned_data["title"]) |
                Q(last_name__icontains=form.cleaned_data["title"])
            )
        return Worker.objects.all()


class WorkerCreateView(generic.CreateView):
    model = Worker
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    form_class = WorkerCreationForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("tasks:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("login")


class TaskTypeListView(generic.ListView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_list.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return TaskType.objects.filter(
                name__icontains=form.cleaned_data["title"]
            )
        return TaskType.objects.all()


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = '__all__'
    success_url = reverse_lazy("tasks:task-type-list")
    template_name = "tasks/task_type_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = '__all__'
    success_url = reverse_lazy("tasks:task-type-list")
    template_name = "tasks/task_type_form.html"


class PositionListView(generic.ListView):
    model = Position
    fields = "__all__"
    template_name = "tasks/position_list.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return Position.objects.filter(
                name__icontains=form.cleaned_data["title"]
            )
        return Position.objects.all()


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = '__all__'
    success_url = reverse_lazy("tasks:position-list")
    template_name = "tasks/position_form.html"


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = '__all__'
    success_url = reverse_lazy("tasks:position-list")
    template_name = "tasks/position_form.html"


class ToggleCompleteTaskView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "tasks/task_detail.html"  # або інша, якщо є

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user in task.assignees.all():
            task.is_complete = not task.is_complete
            task.save()
        return HttpResponseRedirect(reverse_lazy("tasks:task-detail", args=[task.pk]))
