from rest_framework import serializers
from .models import User, Task, TaskHistory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff']


class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'created_at', 'updated_at', 'created_by']


class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = ['task', 'old_status', 'new_status', 'changed_by', 'changed_at']