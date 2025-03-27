from django.urls import include, path
from .views import FirstApiView, ProjectApiView, ProjectDetailApiView, CreateTask, TaskDetail

urlpatterns = [
    path('', FirstApiView.as_view(), name='first- api'),
    path('project/', ProjectApiView.as_view(), name='project'),
    path('project/<int:pk>/', ProjectDetailApiView.as_view(), name='project'),
    path('task/', CreateTask.as_view(), name="create-task"),
    path('task/<int:id>/', TaskDetail.as_view(), name="detail-task")
]