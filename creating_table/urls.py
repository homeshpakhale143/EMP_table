"""
URL configuration for creating_table project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_emp/',display_emp,name='display_emp'),
    path('display_dept/',display_dept, name='display_dept'),
    path('display_salgrade/',display_salgrade,name='display_salgrade'),

    path('display_equijoins/',display_equijoins,name='display_equijoins'),

    path('display_selfjoins/',display_selfjoins,name='display_selfjoins'),

    path('display_EmpMgrDept/',display_EmpMgrDept,name='display_EmpMgrDept'),

    path('display_update/',display_update,name='display_update'),
    
    path('display_delete/',display_delete,name='display_delete'),


    path('display_aggregate/',display_aggregate,name='display_aggregate'),
]
