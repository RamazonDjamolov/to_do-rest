from django.db import models

from common.models import BaseModel

class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, related_name='project_own')
    members = models.ManyToManyField('accounts.User',  related_name='projects', blank=True)

    class Meta:
        db_table = 'projects'
        ordering = ('-created_at',)
