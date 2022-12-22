from django.urls import path 
from apps.todo.views import TodoAPIVIew, ToDoCreateAPIView


urlpatterns = [
    path('', TodoAPIVIew.as_view(), name = "index"),
    path('todo/create/', ToDoCreateAPIView.as_view(), name = "todo_create")
]