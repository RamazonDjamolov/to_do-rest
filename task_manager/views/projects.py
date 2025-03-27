from django.core.serializers import serialize
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from task_manager.models import Project
from task_manager.serializers import ProjectSerializers, ProjectDetailSerializer


# Create your views here.


class FirstApiView(APIView):
    def get(self, request):
        return Response(data={
            'message': 'Hello, World!',
        })

    def post(self, request):
        data = request.data
        print(data, "my data ")
        return Response(data=data)


class ProjectApiView(APIView):
    def get(self, request, pk=None):
        if pk:
            p = get_object_or_404(Project, id=pk)
            serializer = ProjectSerializers(p)
            return Response(serializer.data)
        projects = Project.objects.all()
        serializer = ProjectSerializers(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializers = ProjectSerializers(data=request.data)
        # V1
        # if serializers.is_valid():
        #     serializers.save()
        #     return Response(serializers.data)
        # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        # V2
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    #
    # def put(self, request):
    #     obj = Project.objects.get(pk=request.data.get('id'))
    #     serializers = ProjectSerializers(instance=obj, data=request.data, partial=True)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     return Response(serializers.data, )

    def put(self, request, pk):
        project = get_object_or_404(Project, id=pk)
        serializers = ProjectSerializers(data=request.data, instance=project, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    def delete(self, request, pk):
        project = get_object_or_404(Project, id=pk)
        project.delete()
        return Response({'message': 'deleted successfully'})


class ProjectDetailApiView(APIView):
    def get(self, request, pk):
        p = get_object_or_404(Project, id=pk)
        serializer = ProjectDetailSerializer(p)
        return Response(serializer.data)
