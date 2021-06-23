from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'task-list/',
        'Detail View': 'task-detail/<int:pk>/',
        'Create': 'task-create/',
        'Update': 'task-edit/<int:pk>/',
        'Delete': 'task-delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response('Task does not exist', status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def task_edit(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response('Task deleted', status=status.HTTP_200_OK)
