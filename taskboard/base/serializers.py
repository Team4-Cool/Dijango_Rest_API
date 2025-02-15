from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task, Admin

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['user', 'admin_field']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description']
