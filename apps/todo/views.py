from rest_framework.generics import ListAPIView, ListCreateAPIView
from apps.todo.models import ToDo
from apps.todo.serializers import ToDoSerializer, ToDoCreateSerializer

# Create your views here.
class TodoAPIVIew(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoCreateAPIView(ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoCreateSerializer