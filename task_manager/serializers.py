from rest_framework import serializers

from accounts.models import User
from task_manager.models import Project, Task
from task_manager.models.choice import TaskStatus


class ProjectListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'owner']


class ProjectCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'members', 'description', 'created_at', 'updated_at']


class ProjectUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'members', 'description', 'created_at', 'updated_at']


class ProjectAddMembers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['members']


class ProjectTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", 'status', 'assign_to']


#  taskga tegishli


class ProjecTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'status', 'assign_to']


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'assign_to']


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'status', 'assign_to', 'project']


class ChoiceSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()
