from django.db import models

from accounts.models import User
from common.models import BaseModel
from task_manager.models.choices import TaskStatus


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=250, choices=TaskStatus, default=TaskStatus.TODO)
    assign_to = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, related_name='tasks_assign')
    project = models.ForeignKey('task_manager.Project', on_delete=models.CASCADE, related_name='tasks_project')

    class Meta:
        db_table = 'tasks'
        ordering = ('-created_at',)
