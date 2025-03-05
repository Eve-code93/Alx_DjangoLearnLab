from django.shortcuts import render

from rest_framework import generics
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import your serializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the serializer


from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD actions for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
