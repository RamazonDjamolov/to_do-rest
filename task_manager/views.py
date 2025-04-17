
from django.core.serializers import get_serializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Project
from task_manager.serializers import ProjectListModelSerializer, ProjectCreateModelSerializer, \
    ProjectUpdateModelSerializer


# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListModelSerializer

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.queryset.filter(owner=self.request.user)
        elif self.action == 'project_members':
            return self.queryset.filter(members__exact=self.request.user)  # memberslarni ichida shu user bormi digani
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateModelSerializer
        if self.action in ['update', 'partial_update']:
            return ProjectUpdateModelSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


    @action(methods=['get'], detail = False)
    def project_members(self, request, *args, **kwargs):
        project = self.get_queryset()
        serializer = ProjectListModelSerializer(project, many=True)
        return Response(serializer.data)
