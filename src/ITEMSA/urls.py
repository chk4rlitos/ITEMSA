"""ITEMSA URL Configuration

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
from django.conf import settings
from ITEMSA.apps.Projects.views import login,Dashboard,user_logout,ListPersonal
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login, name='login'),    
    path(('dashboard/((<pk>)[0-9]+)'), login_required(Dashboard.as_view()), name='dashboard'),
    path(('dashboard/(<pk>[0-9]+)/Lista-Personal'), login_required(ListPersonal.as_view()), name='listar_personal'),
    path('logout', user_logout, name='logout'),
    path('admin/', admin.site.urls)
]
