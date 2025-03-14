from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List and Create Books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to view books, but only authenticated users can add books
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Retrieve, Update, Delete a Book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to view books, but only authenticated users can edit or delete
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]  # Allow only admin users to create books

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]  # Restrict edit/delete to admins


from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly  # Custom permission for admin-only actions

# Alias DRF views to match expected Django class-based view names
class ListView(generics.ListCreateAPIView):  # List + Create
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UpdateView(generics.UpdateAPIView):  # Update only
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

class DeleteView(generics.DestroyAPIView):  # Delete only
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
