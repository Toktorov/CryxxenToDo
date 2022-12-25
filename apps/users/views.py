from django.shortcuts import render
from apps.users.models import User
from apps.users.serializer import UserSerializer, UserRegisterSerializer, UserDetailSerializer, UserUpdateSerializer
from apps.users.permissions import IsUserPermissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import filters

# Create your views here.
class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )
    filter_backends = [filters.SearchFilter]
    search_fields = ('username', 'email', 'phone_number', 'age')

class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny, )

class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsUserPermissions, )

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsUserPermissions, )

class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsUserPermissions, )