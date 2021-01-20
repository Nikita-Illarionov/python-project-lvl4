from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.TasksList.as_view(), name='tasks'),
    path('create/', views.CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),
]