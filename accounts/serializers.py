from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 're_password']

    def validate(self, attrs):
        re_password = attrs.pop('re_password')
        password = attrs.get('password')
        if re_password != password:
            raise ValidationError("password not equal re password")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']