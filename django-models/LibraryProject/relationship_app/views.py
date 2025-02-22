

from django.shortcuts import render
from .models import Book


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  # Django's built-in login form
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to a home page (change 'home' to your actual homepage URL name)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # Django's built-in user registration form
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log in the new user automatically
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


