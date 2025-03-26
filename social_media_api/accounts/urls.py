from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistrationView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),  # ✅ Registration
    path('login/', obtain_auth_token, name='login'),  # ✅ Login using DRF token auth
    path('profile/', UserProfileView.as_view(), name='profile'),  # ✅ Profile management
]
