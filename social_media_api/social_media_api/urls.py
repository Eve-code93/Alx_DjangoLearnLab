"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from posts.views import like_post, unlike_post, home  # ✅ Import home view

urlpatterns = [
    path('', home, name='home'),  # ✅ Define the home URL
    path('like/<int:pk>/', like_post, name='like-post'),
    path('unlike/<int:pk>/', unlike_post, name='unlike-post'),
]
