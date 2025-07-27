from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from tasks.models import Worker, Task


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control"
            }
        ),
        input_formats=["%Y-%m-%dT%H:%M"]
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskCreateForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
        )


class WorkerUpdateForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email", "position")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["tasks"].initial = self.instance.tasks.all()

    def save(self, commit=True):
        worker = super().save(commit=False)
        if commit:
            worker.save()
        worker.tasks.set(self.cleaned_data["tasks"])
        return worker


class SearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "class": "form-control me-2",
            "placeholder": "Search",
            "aria-label": "Search"
        })
    )
