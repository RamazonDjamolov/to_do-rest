from django.urls import path
from rest_framework.routers import DefaultRouter

from task_manager.views import ProjectViewSet, TaskViewSet, TaskStatusViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='projects')
router.register('task', TaskViewSet, basename='tasks')
router.register('task-statuses', TaskStatusViewSet, basename='task-status')

urlpatterns = [
                  # path('/', UserCreateView.as_view(), name='signup'),
              ] + router.urls
