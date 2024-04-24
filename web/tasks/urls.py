# Django
from django.urls import path, include
# Django REST framework
from rest_framework.routers import DefaultRouter
# Views
from .views import TasksViewSet

router = DefaultRouter()
router.register(r'tasks', TasksViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls))
]