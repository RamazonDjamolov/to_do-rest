from django.urls import path
from rest_framework.routers import DefaultRouter

from task_manager.views import ProjectViewSet, TaskViewSet, TaskStatusViewSet, TestCelery

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='projects')
# router.register('task', TaskViewSet, basename='tasks')
router.register('task-statuses', TaskStatusViewSet, basename='task-status')
router.register('test', TestCelery, basename='test')

urlpatterns = [
                  # path('/', UserCreateView.as_view(), name='signup'),
              ] + router.urls
