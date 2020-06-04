"""SihProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .router import router
from rest_framework.authtoken import views
from django.contrib.auth.views import LoginView
from proj.views import UserRegister, CheckOnlyGovernMentView, CheckOnlyNgoView
from proj.api.viewsets import getNGOList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ngoslist/', getNGOList.as_view(), name='ngo-list'),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-auth-token'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegister, name='register'),
    path('gov/', CheckOnlyGovernMentView, name='gov-view'),
    path('ngo/', CheckOnlyNgoView, name='ngo-view'),
]