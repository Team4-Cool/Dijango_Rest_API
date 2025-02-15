from rest_framework import viewsets
from .models import Task, Admin, User
from .serializers import UserSerializer, AdminSerializer, TaskSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
