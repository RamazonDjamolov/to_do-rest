from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import UserCreateView, UserViewSet
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('', UserCreateView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls