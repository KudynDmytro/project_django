"""test_project URL Configuration

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
from django.urls import path
from django.contrib import admin
from django.urls import path
from test_app.views import hello
from test_app.views import gen_password
from test_app.views import get_customers
from test_app.views import get_unique_name
from test_app.views import get_value

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', admin.site.urls),
    path('password/', gen_password),
    path('customers/', get_customers),
    path('unique/', get_unique_name),
    path('value/', get_value)
]
