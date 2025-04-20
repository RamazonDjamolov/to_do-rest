from rest_framework import serializers

from accounts.models import User
from task_manager.models import Project, Task


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

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", 'description', 'status', 'assign_to', 'project']


