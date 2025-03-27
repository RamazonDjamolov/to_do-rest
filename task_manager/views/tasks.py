from django.core.serializers import serialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from task_manager.serializers import CreateTaskSerializer, DetailTaskSerializer
from task_manager.models import Task


class CreateTask(APIView):
    def get(self, request):
        obj = Task.objects.all()
        serializer = CreateTaskSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serialize = CreateTaskSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        return Response(serialize.data)


class TaskDetail(APIView):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = DetailTaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = DetailTaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
