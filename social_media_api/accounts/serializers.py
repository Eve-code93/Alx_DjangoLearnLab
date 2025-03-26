from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()  # This dynamically fetches the user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Create a new user
        Token.objects.create(user=user)  # Generate an authentication token for the new user
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Field for the username
    password = serializers.CharField()  # Field for the password
