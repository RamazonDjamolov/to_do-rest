from rest_framework import serializers

from task_manager.models import Task
from task_manager.serializers.projects import ProjectSerializers


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', "description", "assign_to", "project")


class DetailTaskSerializer(serializers.ModelSerializer):
    # project = ProjectSerializers()

    class Meta:
        model = Task
        fields = ('id', 'title', "description", "assign_to", "project")

    def update(self, instance, validated_data):
        Task.objects.update(**validated_data)
        return instance
