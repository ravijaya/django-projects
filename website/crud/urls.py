"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employee, name="list_employee"),
    path('add/', views.add_form, name="create_form"),
    path('edit/<int:pk>', views.edit_employee, name="edit_employee"),
    path('delete/<int:pk>', views.delete_employee, name="delete_employee"),
    path('details/<int:pk>', views.employee_details, name="employee_details"),
]
