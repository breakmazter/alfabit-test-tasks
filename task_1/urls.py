from django.urls import path

from task_1 import views

urlpatterns = [
    path('1', views.index, name='index'),
]
