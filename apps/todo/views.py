from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.todo.models import ToDo
from apps.todo.serializers import ToDoSerializer, ToDoCreateSerializer
from apps.todo.permissions import IsOwnerPermissions

# Create your views here.
class TodoAPIView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermissions, )

class ToDoCreateAPIView(ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoCreateSerializer
    permission_classes = (IsOwnerPermissions, )