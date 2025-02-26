from django.urls import path
from .views import TaskListCreate, TaskDetail, UserList

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('users/', UserList.as_view(), name='user-list'),
]