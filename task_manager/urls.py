from django.urls import path
from rest_framework.routers import DefaultRouter

from task_manager.views import ProjectViewSet


router = DefaultRouter()
router.register('project', ProjectViewSet, basename='projects')


urlpatterns = [
    # path('/', UserCreateView.as_view(), name='signup'),
]+router.urls