from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
 
from django.urls import path
from .views import user_login, user_logout, register
from django.contrib.auth.views import LogoutView  # Django's built-in logout view

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
]
