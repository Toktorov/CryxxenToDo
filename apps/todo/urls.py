from django.urls import path 
from apps.todo.views import TodoAPIView, ToDoCreateAPIView


urlpatterns = [
    path('api/todo/', TodoAPIView.as_view(), name = "index"),
    path('api/todo/create/', ToDoCreateAPIView.as_view(), name = "todo_create")
]