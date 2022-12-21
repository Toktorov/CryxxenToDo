from rest_framework.generics import ListAPIView
from apps.todo.models import ToDo
from apps.todo.serializers import ToDoSerializer

# Create your views here.
class TodoAPIVIew(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer