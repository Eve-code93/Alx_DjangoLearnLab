from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # User Registration
    path('register/', views.register, name='register'),
    
    # User Profile
    path('profile/', views.profile, name='profile'),
]
