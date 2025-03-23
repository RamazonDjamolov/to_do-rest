from django.db import models

class TaskStatus(models.TextChoices):
    TODO = 'todo', 'TODO'
    IN_PROGRESS = 'in_progress', 'IN PROGRESS'
    DONE = 'done', 'DONE'
    REJECTED = 'rejected', 'REJECTED'
