# Django REST Framework
from rest_framework import serializers
# Models
from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=5, max_length=100, required=True)
    description = serializers.CharField(min_length=10, max_length=500, required=False)

    class Meta:
        model = Tasks
        fields = (
            'name',
            'description',
        )
