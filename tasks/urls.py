from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('tags/', views.tag_page, name='tags'),
    path('create_tag/', views.create_tag, name='create_tag'),
    path('tags/<int:pk>/update', views.TagUpdateView.as_view(), name='update_tag'),
    path('tags/<int:pk>/delete', views.TagDeleteView.as_view(), name='delete_tag'),
]
