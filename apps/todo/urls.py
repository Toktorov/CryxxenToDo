from django.urls import path 
from apps.todo.views import TodoAPIVIew


urlpatterns = [
    path('', TodoAPIVIew.as_view(), name = "index")
]