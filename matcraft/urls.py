"""matcraft URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('blog/',views.blog),
    path('register/',views.register),
    path('login/',views.login),
    path('verify/',views.verify),
    path('user/', include('user.urls')),
    path('myadmin/', include('myadmin.urls')),
    path('mainshop/',views.mainshop),
    path('home/',views.home),
    path('get1/',views.get1),
    path('get2/',views.get2),
    path('get3/',views.get3),
    path('get4/',views.get4),
    path('get5/',views.get5),
    path('get6/',views.get6),
    path('get7/',views.get7),
    path('get8/',views.get8),
    path('get9/',views.get9),
    path('get10/',views.get10),
    path('get11/',views.get11),
    path('get12/',views.get12),
    path('get13/',views.get13),
    path('get14/',views.get14),
    path('get15/',views.get15),
]
