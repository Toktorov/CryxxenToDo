from django.shortcuts import render
from apps.users.models import User
from apps.users.serializer import UserSerializer, UserRegisterSerializer
from rest_framework.generics import ListAPIView, CreateAPIView

# Create your views here.
class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer