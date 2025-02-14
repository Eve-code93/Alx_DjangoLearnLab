# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book instance (assuming we know its ID)
book = Book.objects.get(id=1)  # Change 1 to the actual book ID if needed

# Delete the book instance
book.delete()

# Verify deletion
print(Book.objects.all())  # Should return an empty queryset if no books exist

