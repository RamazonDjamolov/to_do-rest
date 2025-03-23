from django.urls import include, path
from .views import FirstApiView ,ProjectApiView
urlpatterns = [
    path('', FirstApiView.as_view(), name='first- api'),
    path('project/', ProjectApiView.as_view(), name='project'),
]