from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


def home(request):
    return HttpResponse("Welcome to the Social Media API")
# ✅ Fetch the custom user model dynamically
CustomUser = get_user_model()

# ✅ Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ✅ Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ✅ User Feed View
class UserFeedView(generics.ListAPIView):
    """Generates a feed of posts from followed users"""
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")

# ✅ Like Post API
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create notification for the post owner
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked",
        target=post
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

# ✅ Unlike Post API
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    like = Like.objects.filter(user=request.user, post=post).first()
    if like:
        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)

    return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
