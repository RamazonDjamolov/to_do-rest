from django.db import models


class TaskStatus(models.TextChoices):
    TODO = 'todo', 'TODO'
    IN_PROGRESS = 'in_progress', 'IN_PROGRESS'
    DONE = 'done', 'Done'
    REJECTED = 'rejected', 'Rejected'
