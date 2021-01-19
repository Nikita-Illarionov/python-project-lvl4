from django.urls import path
from . import views


urlpatterns = [
    path('', views.LabelView.as_view(), name='labels'),
    path('create/', views.create_label, name='create_label'),
    path('<int:pk>/update/', views.UpdateLabel.as_view(), name='update_label'),
    path('<int:pk>/delete/', views.DeleteLabel.as_view(), name='delete_label'),
]
