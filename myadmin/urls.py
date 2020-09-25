from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminhome),
    path('addpro/',views.addpro),
    path('editpro/',views.editpro),
    path('editinfo/',views.editinfo),
]