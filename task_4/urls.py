from django.urls import path

from task_4 import views

urlpatterns = [
    path('4', views.index, name='index'),
]
