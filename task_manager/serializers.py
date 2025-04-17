from rest_framework import serializers

from task_manager.models import Project


class ProjectListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','name', 'description', 'created_at', 'updated_at', 'owner']


class ProjectCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'members', 'description', 'created_at', 'updated_at']


class ProjectUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'members', 'description', 'created_at', 'updated_at']
