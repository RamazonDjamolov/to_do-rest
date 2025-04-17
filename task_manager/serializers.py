from rest_framework import serializers

from task_manager.models import Project


class ProjectListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'created_at', 'updated_at']


class ProjectCreateModelSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'created_at', 'updated_at']
