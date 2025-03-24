from rest_framework import serializers

from task_manager.models import Project


# Custom serializers
class ProjectSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Project.objects.create(name=validated_data.get('name'), description=validated_data.get('description'))

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}
        if self.instance:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance
