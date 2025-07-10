from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workers",
    )

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return self.username


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    name = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(
        default=False
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="Medium"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    assignees = models.ManyToManyField(
        Worker,
        related_name="tasks",
        blank=True
    )

    def __str__(self):
        return self.name
