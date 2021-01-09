from django.contrib import admin
from django.urls import path

from weather_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name= 'delete')

]
