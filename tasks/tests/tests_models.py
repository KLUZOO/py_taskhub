from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from tasks.models import Task, Worker, TaskType, Position


class ModelTest(TestCase):
    def setUp(self):
        self.position_QA = Position.objects.create(name="QA")
        self.position_designer = Position.objects.create(name="Designer")
        self.position_devops = Position.objects.create(name="DevOps")
        self.position_project_manager = Position.objects.create(name="Project manager")
        self.position_developer = Position.objects.create(name="Developer")
        self.task_type_bug = TaskType.objects.create(name="Bug")
        self.task_type_new_feature = TaskType.objects.create(name="New feature")
        self.task_type_breaking = TaskType.objects.create(name="Breaking change")
        self.task_type_refactoring = TaskType.objects.create(name="Refactoring")
        self.task_type_QA = TaskType.objects.create(name="QA")
        self.client = Client()
        self.admin_test = get_user_model().objects.create_superuser(
            username="admin_test",
            password="admin12345678",
            position=self.position_devops,
            first_name="Admin",
            last_name="Test",
            email="admintest@test.com",
        )
        self.client.force_login(self.admin_test)
        self.user_ivan = get_user_model().objects.create_user(
            username="ivan",
            password="ivan12345678",
            position=self.position_devops,
            first_name="Ivan",
            last_name="Test",
            email="ivantest@test.com",
        )
        self.user_sasha = get_user_model().objects.create_user(
            username="sasha",
            password="sasha12345678",
            position=self.position_devops,
            first_name="Sasha",
            last_name="Test",
            email="sashatest@test.com",
        )
        self.task_one = Task.objects.create(
            name="Task one",
            description="Some description one",
            deadline=datetime.now(),
            priority="High",
            task_type=self.task_type_bug,
        )
        self.task_one.assignees.add(self.user_ivan)
        self.task_one.save()
        self.task_two = Task.objects.create(
            name="Task two",
            description="Some description two",
            deadline=datetime.now(),
            priority="Low",
            task_type=self.task_type_new_feature,
        )
        self.task_two.assignees.add(self.user_sasha)
        self.task_two.save()

    def test_worker_model(self):
        worker_max = get_user_model().objects.create_user(
            username="max",
            password="max12345678",
            position=self.position_devops,
            first_name="Max",
            last_name="Test",
            email="maxtest@test.com",
        )
        self.assertEqual(str(worker_max), str(worker_max.username))
