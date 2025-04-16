from django.db import models

from common.models import BaseModel
from task_manager.models.choice import TaskStatus


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=TaskStatus.choices, default=TaskStatus.TODO)
    assign_to = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, related_name='task_assign', null=True)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name='task_project')

    class Meta:
        db_table = 'task'
        ordering = ('-created_at',)
