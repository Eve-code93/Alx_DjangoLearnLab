from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Post

User = get_user_model()

class LikePostTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(author=self.user, content="Test post")
        self.client.force_authenticate(user=self.user)

    def test_like_post(self):
        response = self.client.post(f"/posts/{self.post.id}/like/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unlike_post(self):
        self.client.post(f"/posts/{self.post.id}/like/")
        response = self.client.delete(f"/posts/{self.post.id}/unlike/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
