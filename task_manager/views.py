from django.core.serializers import get_serializer
from django.shortcuts import render
from rest_framework import viewsets

from task_manager.models import Project
from task_manager.serializers import ProjectListModelSerializer, ProjectCreateModelSerilizer


# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListModelSerializer



    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListModelSerializer
        if self.action == 'create':
            return ProjectCreateModelSerilizer
        return self.serializer_class

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

