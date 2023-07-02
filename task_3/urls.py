from django.urls import path

from task_3 import views

urlpatterns = [
    path('3', views.index, name='index'),
]
