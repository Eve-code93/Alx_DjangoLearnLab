from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
 
from django.urls import path
from .views import register_view

urlpatterns = [
    path("register/", register_view, name="register"),
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
    path('admin-dashboard/', admin_view.admin, name='admin_dashboard'),
]

from django.urls import path
from relationship_app.views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view.librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_view.member_dashboard, name='member_dashboard'),
]
from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
from django.urls import path
from . import admin_view  # Ensure admin_view is in the same app directory

urlpatterns = [
    path('admin-dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
]
def is_admin(user):
    if user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin':
        return True
    return redirect('login')  # Redirect unauthorized users to login page

from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),  # Add Book URL
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit Book URL
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete Book URL
]

