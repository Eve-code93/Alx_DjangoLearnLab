from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
 
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # User Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]


from django.urls import path
from relationship_app.views import admin_view

urlpatterns = [
    path('admin-dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
]

from django.urls import path
from relationship_app.views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view.librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_view.member_dashboard, name='member_dashboard'),
]
