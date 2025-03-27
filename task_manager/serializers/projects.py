from prompt_toolkit.validation import ValidationError
from rest_framework import serializers

from accounts.serializers import UserSerializer
from task_manager.models import Project


# Custom serializers
class ProjectSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    updated_at = serializers.DateTimeField(read_only=True)

    def validate(self, data):
        if len(data.get('name')) <= 3:
            raise serializers.ValidationError('name qatorini charlari 3 tadan kam ')
        return data

    def create(self, validated_data):
        return Project.objects.create(name=validated_data.get('name'), description=validated_data.get('description'))

    def update(self, instance, validated_data):
        # version 1
        # instance.name = validated_data.get('name', instance.name)
        # instance.description = validated_data.get('description', instance.description)
        # instance.save()
        # return instance

        # orginal version v2

        Project.objects.filter(pk=instance.pk).update(**validated_data)
        return instance

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}
        if self.instance:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance


#
# class ProjectDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     owner = serializers.IntegerField()
#     members = serializers.RelatedField(many=True, read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)


class ProjectDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'owner', 'members', 'updated_at')
