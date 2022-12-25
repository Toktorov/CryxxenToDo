from django.urls import path 
from apps.users.views import UserAPIView, UserRegisterAPIView, UserDetailAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/users/', UserAPIView.as_view(), name = "api_users"),
    path('api/users/<int:pk>/', UserDetailAPIView.as_view(), name = "api_users_detail"),
    path('api/users/update/<int:pk>/', UserUpdateAPIView.as_view(), name = "api_users_update"),
    path('api/users/destroy/<int:pk>/', UserDestroyAPIView.as_view(), name = "api_users_destroy"),
    #auth
    path('api/users/register/', UserRegisterAPIView.as_view(), name = "api_users_register"),
    path('api/users/login/', TokenObtainPairView.as_view(), name='api_login'),
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]