from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from .serializers import TaskSerializer
from .models import Task
from api import serializers

# Overview of API endpoints
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

# Task list view
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()  # Get all tasks
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# Detail list view
@api_view(['GET'])
def taskDetail(request, pk):
    try:
        task = Task.objects.get(id=pk)  # Fetch the task with the given primary key
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)

# create task view
@api_view(['POST'])
def taskCreate(request, pk):
    try:
        task = Task.objects.get(id=pk)  # Fetch the task with the given primary key
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)
    
# update task view
@api_view(['POST'])
def taskUpdate(request, pk):
    try:
        task = Task.objects.get(id=pk)  # Fetch the task with the given primary key
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)
    
# delete task view
@api_view(['DELETE'])
def taskDelete(request, pk):
        task = Task.objects.get(id=pk)  # Fetch the task with the given primary key
        task.delete()
        return Response(serializers.data)
        
 

