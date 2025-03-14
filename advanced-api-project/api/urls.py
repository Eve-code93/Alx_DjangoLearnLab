from django.urls import path
from .views import AuthorListCreateView, BookListCreateView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
]
from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
