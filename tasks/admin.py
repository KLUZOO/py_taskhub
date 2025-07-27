from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Worker, Position, TaskType, Task


@admin.register(Worker)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Position)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(TaskType)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Task)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name", "priority", "task_type")
