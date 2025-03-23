from rest_framework.response import Response
from rest_framework.views import APIView

from task_manager.models import Project


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
    def get(self, request):
        projects = Project.objects.all()
        data = [
            {
                'id': p.id,
                'name': p.name,
                'description': p.description,

            } for p in projects
        ]
        return Response(data=data)
