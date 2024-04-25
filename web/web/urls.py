
"""The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing, name="landing"),
    path('post_agregar/',post_agregar, name="post_agregar"),
    path('modificar/', modificar, name='modificar'),
    path('modificar/modificar_pan/<int:pk>/', modificar_pan, name='modificar_pan'),    
    path('api-auth/', include('rest_framework.urls')),
    #path('', include(('tasks.urls', 'tasks'), namespace = 'tasks')),
    #path('meseros', include(('meseros.urls', 'meseros'), namespace = 'meseros')),
    path('calculadora/', calc, name='calculadora')
]