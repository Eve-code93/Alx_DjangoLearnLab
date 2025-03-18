from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm  # ✅ Ensure this import is correct

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "blog/profile.html")

def home(request):
    return render(request, "blog/home.html")  # ✅ Ensure this template exists


from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# List all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # Template to display all posts
    context_object_name = "posts"
    ordering = ["-created_at"]  # Newest posts first

# Show a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"  # Template to display a single post

# Create a new post (Authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"  # Template for creating/editing a post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to logged-in user
        return super().form_valid(form)

# Update a post (Only the author can edit)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the author to edit

# Delete a post (Only the author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")  # Redirect after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the author to delete
