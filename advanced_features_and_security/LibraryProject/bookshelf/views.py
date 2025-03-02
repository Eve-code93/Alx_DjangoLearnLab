from django.shortcuts import render

# Create your views here.
# LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Your book creation logic here
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your book editing logic here
    return render(request, 'bookshelf/book_edit.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your book deletion logic here
    pass
# LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Ensure proper validation and sanitization of user input
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Ensure proper validation and sanitization of user input
    return render(request, 'bookshelf/book_edit.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Ensure proper validation and sanitization of user input
    pass
# LibraryProject/bookshelf/views.py
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

# LibraryProject/bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle form data
            return redirect('success_url')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})
