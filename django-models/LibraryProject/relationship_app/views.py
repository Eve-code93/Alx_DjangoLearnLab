

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

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to homepage (change as needed)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to homepage
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden
from relationship_app.models import UserProfile

# Check if user is an Admin
def is_admin(user):
    return UserProfile.objects.filter(user=user, role='Admin').exists()

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_dashboard.html')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.models import UserProfile

# Check if user is a Librarian
def is_librarian(user):
    return UserProfile.objects.filter(user=user, role='Librarian').exists()

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_dashboard.html')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.models import UserProfile

# Check if user is an Admin
def is_admin(user):
    return UserProfile.objects.filter(user=user, role='Admin').exists()

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_dashboard.html')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.models import UserProfile

# Check if user is a Member
def is_member(user):
    return UserProfile.objects.filter(user=user, role='Member').exists()

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'relationship_app/member_dashboard.html')
