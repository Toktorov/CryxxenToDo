from django.urls import path 
from apps.users.views import UserAPIView, UserRegisterAPIView


urlpatterns = [
    path('api/users/', UserAPIView.as_view(), name = "api_users"),
    path('api/users/register/', UserRegisterAPIView.as_view(), name = "api_users_register")
]