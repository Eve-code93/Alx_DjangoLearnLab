from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, UserSerializer
from posts.models import Post
from posts.serializers import PostSerializer

# Reference the custom user model
CustomUser = get_user_model()

### User Authentication Views

class RegisterView(generics.CreateAPIView):
    """User registration view"""
    queryset = CustomUser.objects.all()  # Use CustomUser model
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    """User login view"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateAPIView):
    """Retrieve and update user profile"""
    queryset = CustomUser.objects.all()  # Use CustomUser model
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


### Follow/Unfollow Views

class FollowUserView(generics.GenericAPIView):
    """Follow another user"""
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Retrieve the user to follow using CustomUser model
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        # Prevent following oneself
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the following list
        request.user.following.add(user_to_follow)
        return Response({"message": "You are now following this user."}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """Unfollow a user"""
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Retrieve the user to unfollow using CustomUser model
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        # Prevent unfollowing oneself
        if request.user == user_to_unfollow:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the user from the following list
        request.user.following.remove(user_to_unfollow)
        return Response({"message": "You have unfollowed this user."}, status=status.HTTP_200_OK)


### Post Views

class PostListView(generics.ListCreateAPIView):
    """List all posts or create a new post"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a post"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikePostView(APIView):
    """Like a post"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if post.likes.filter(id=user.id).exists():
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.add(user)
        return Response({"message": "Post liked successfully."}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    """Unlike a post"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if not post.likes.filter(id=user.id).exists():
            return Response({"error": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.remove(user)
        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
