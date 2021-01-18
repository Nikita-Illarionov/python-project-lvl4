from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('statuses/', views.status_page, name='statuses'),
    path('tags/', views.tag_page, name='tags'),
    path('create_status/', views.create_status, name='create_status'),
    path('statuses/<int:pk>/update', views.StatusUpdateView.as_view(), name='update_status'),
    path('statuses/<int:pk>/delete', views.StatusDeleteView.as_view(), name='delete_status'),
    path('create_tag/', views.create_tag, name='create_tag'),
    path('tags/<int:pk>/update', views.TagUpdateView.as_view(), name='update_tag'),
    path('tags/<int:pk>/delete', views.TagDeleteView.as_view(), name='delete_tag'),
]
