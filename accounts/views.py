from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from accounts.models import User
from accounts.serializers import UserCreateSerializer
from accounts.serializers import UserSerializer


class UserCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserCreateSerializer






# Create your views here.
class UserViewSet(GenericViewSet, ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]