"""Degime_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
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
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from user_app.views import CheckAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/check/', CheckAPIView.as_view(), name='Backend API Check'),
    
    path('api/social/', include('social_app.urls')),
    
    path('api/chat/', include('chat_app.urls')),
    
    path('api/account/', include('user_app.urls')),

    path('api/shop/', include('shop_app.urls')),
    
    path('api/docs/', include_docs_urls(title='DEGIME_API')),
    path('schema/', get_schema_view(
        title="DEGIME_API", description="Guide for the CRUD operations",
        version="1.0.0"), name='OpenApi_Schema')
]
