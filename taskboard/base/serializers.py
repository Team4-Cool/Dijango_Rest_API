from rest_framework import serializers
from .models import Task, User, Admin

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
        fields = ['name', 'description', 'status']