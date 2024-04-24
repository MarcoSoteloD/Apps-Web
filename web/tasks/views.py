
# Django Rest Framework
from rest_framework import viewsets
from django.shortcuts import render
# Models
from .models import Tasks
# Serializer
from .serializers import TasksSerializer


class TasksViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing tasks.
    """
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer