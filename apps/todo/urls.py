from django.urls import path 
from apps.todo.views import TodoAPIView, ToDoCreateAPIView, TodoUpdateAPIView, ToDoDestroyAPIView, ToDoAllDestroyAPIView


urlpatterns = [
    path('api/todo/', TodoAPIView.as_view(), name = "index"),
    path('api/todo/create/', ToDoCreateAPIView.as_view(), name = "todo_create"),
    path('api/todo/update/<int:pk>/', TodoUpdateAPIView.as_view(), name = "todo_update"),
    path('api/todo/destroy/<int:pk>/', ToDoDestroyAPIView.as_view(), name = "todo_destroy"),
    path('api/todo/destroy/all/', ToDoAllDestroyAPIView.as_view(), name = "todo_all_destroy")
]