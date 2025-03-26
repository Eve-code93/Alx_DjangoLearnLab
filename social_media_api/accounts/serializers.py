from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Dynamically fetch the user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Use get_user_model().objects.create_user to create a secure user instance
        user = User.objects.create_user(**validated_data)
        # Generate a token for the new user
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Define field for 'username'
    password = serializers.CharField()  # Define field for 'password'
