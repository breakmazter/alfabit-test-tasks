from django.contrib import admin
from django.urls import include
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('task/', include('task_1.urls')),
    path('task/', include('task_2.urls')),
    path('task/', include('task_3.urls')),
    path('task/', include('task_4.urls')),
]
