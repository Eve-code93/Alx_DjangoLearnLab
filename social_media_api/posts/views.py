from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

CustomUser = get_user_model()

class UserFeedView(generics.ListAPIView):
    """Generates a feed of posts from followed users"""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Get users the current user follows
        return Post.objects.filter(author__in=following_users).order_by("-created_at")  # Ensure this line is present

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from notifications.models import Notification

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  # Ensure post exists
    user = request.user
    
    # Ensure user hasn't already liked the post
    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Generate a notification
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb="liked",
        target=post
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)  # Ensure post exists
    user = request.user
    
    # Check if user has liked the post
    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
