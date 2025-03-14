from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test client and test data."""
        self.client = APIClient()

        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2022)

        # Authenticate user
        self.client.login(username="testuser", password="testpassword")

    def test_get_all_books(self):
        """Test retrieving all books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        """Test retrieving a single book"""
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book(self):
        """Test creating a book"""
        book_data = {"title": "Book Three", "author": "Author C", "publication_year": 2021}
        response = self.client.post("/api/books/create/", book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

