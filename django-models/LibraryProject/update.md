# Update a Book Instance

## Command:
```python
book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id).title)
# Output: Nineteen Eighty-Four
