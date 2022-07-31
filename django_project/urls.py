"""django_project URL Configuration

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
from django_project.datacenter.active_passcards_view import active_passcards_view
from django_project.datacenter.passcard_info_view import passcard_info_view
from django_project.datacenter.storage_information_view import storage_information_view
from django.urls import path

urlpatterns = [
    path('', active_passcards_view, name='active_passcards'),
    path('storage_information', storage_information_view, name='storage_information'),
    path('passcard_info/<uuid:passcode>', passcard_info_view, name='passcard_info'),
    path('in_storage_now', storage_information_view, name='storage_information'),

]
