# Retrieve a Book Instance

## Command:
# Get all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
