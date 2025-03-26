from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ Ensure CharField is present

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        """Create a new user and generate a token"""
        user = get_user_model().objects.create_user(**validated_data)  # ✅ Using create_user()
        Token.objects.create(user=user)  # ✅ Generate authentication token
        return user

