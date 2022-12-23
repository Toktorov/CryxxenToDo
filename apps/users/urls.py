from django.urls import path 
from apps.users.views import UserAPIView, UserRegisterAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/users/', UserAPIView.as_view(), name = "api_users"),
    #auth
    path('api/users/register/', UserRegisterAPIView.as_view(), name = "api_users_register"),
    path('api/login/', TokenObtainPairView.as_view(), name='api_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]