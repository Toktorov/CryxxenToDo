from django.urls import path 
from apps.todo.views import TodoAPIVIew, ToDoCreateAPIView


urlpatterns = [
    path('api/todo/', TodoAPIVIew.as_view(), name = "index"),
    path('api/todo/create/', ToDoCreateAPIView.as_view(), name = "todo_create")
]