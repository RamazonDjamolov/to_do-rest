from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets

from accounts.permissions import IsOwner, IsMembers
from accounts.serializers import UserSerializer
from .models import Project, Task
from task_manager.serializers import ProjectListModelSerializer, ProjectCreateModelSerializer, \
    ProjectUpdateModelSerializer, ProjectAddMembers, ProjectTasksSerializer, TaskListSerializer, \
    ProjecTaskCreateSerializer, CreateTaskSerializer,  ChoiceSerializer
from .models.choice import TaskStatus


# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.queryset.filter(owner=self.request.user)
        elif self.action == 'my_project_members':
            return self.queryset.filter(members__exact=self.request.user)  # memberslarni ichida shu user bormi digani
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateModelSerializer
        if self.action in ['update', 'partial_update']:
            return ProjectUpdateModelSerializer
        if self.action == 'project_add_members':
            return ProjectAddMembers
        elif self.action == 'project_create_task':
            return ProjecTaskCreateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'project_add_members':
            return [IsAuthenticated, IsOwner]
        return super(ProjectViewSet, self).get_permissions()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def perform_project_add_members(self, serializer, project):
        return serializer.save(project=project)

    #  user azo bolgan projectlar va uzini projectlari
    @action(methods=['get'], detail=False, )
    def my_project_members(self, request, *args, **kwargs):
        project = self.get_queryset()
        serializer = ProjectListModelSerializer(project, many=True)
        return Response(serializer.data)

    @action(methods=['put'], detail=True, serializer_class=ProjectAddMembers,
            permission_classes=[IsAuthenticated, IsOwner])
    def project_add_members(self, request, pk=None):
        project = self.get_object()
        serializer = ProjectAddMembers(data=request.data, instance=project, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # shu projectni korish ichun memberlar (azolar yoki owner) korish uchun pasda
    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated, IsOwner | IsMembers])
    def project_members(self, request, pk=None):
        project = self.get_object()  # get object pk keganda iwlatilinadi faqat shu projectni olish uchun
        user = project.members.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated, IsOwner | IsMembers])
    def project_tasks(self, request, pk=None):
        project = self.get_object()
        tasks = Task.objects.all().filter(project=project)
        serializer = ProjectTasksSerializer(tasks, many=True)
        return Response(serializer.data)

    # @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated, IsOwner | IsMembers])
    # def project_create_task(self, request, pk=None):
    #     project = self.get_object()
    #     serializer = ProjecTaskCreateSerializer(data=request.data)
    #     serializer.project = project
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


#


class TaskViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskListSerializer
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateTaskSerializer
        return self.serializer_class




class TaskStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        choices = TaskStatus.choices
        serializer = ChoiceSerializer(
            [{"value": value, "label": label} for value, label in choices],
            many=True
        )
        return Response(serializer.data)
