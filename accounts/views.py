from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView, ListCreateAPIView

from accounts.models import User
from accounts.serializers import UserCreateSerializer


class UserCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserCreateSerializer






# Create your views here.
