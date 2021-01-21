from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_table, name='users'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('create/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/delete', views.UserDeleteView.as_view(), name='delete_user'),
]
