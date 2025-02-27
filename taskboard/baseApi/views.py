from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Task, User, TaskHistory
from .serializers import TaskSerializer, UserSerializer


class TaskListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        status_filter = request.query_params.get('status', None)
        tasks = Task.objects.filter(created_by=request.user)
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk, created_by=self.request.user)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Task not found or access denied'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Task not found or access denied'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Task not found or access denied'}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskMove(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, created_by=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found or access denied'}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get('status')
        if new_status not in [choice[0] for choice in Task.STATUS_CHOICES]:
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

        if task.status == 'DONE' and new_status == 'TASK':
            return Response({'error': 'Cannot move task from DONE to TASK'}, status=status.HTTP_400_BAD_REQUEST)

        TaskHistory.objects.create(
            task=task,
            old_status=task.status,
            new_status=new_status,
            changed_by=request.user
        )

        task.status = new_status
        task.save()

        return Response({'status': 'Task moved successfully'}, status=status.HTTP_200_OK)


class UserList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)