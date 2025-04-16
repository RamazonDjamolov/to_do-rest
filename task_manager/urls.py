from django.urls import path
from rest_framework.routers import DefaultRouter

# from accounts.views import UserCreateView

router = DefaultRouter()
# router.register('users', UserCreateView, basename='register')


urlpatterns = [
    # path('/', UserCreateView.as_view(), name='signup'),
]+router.urls