from django.urls import path

from task_2 import views

urlpatterns = [
    path('2', views.index, name='index'),
]
