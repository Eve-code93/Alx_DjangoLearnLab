from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()  # Dynamically fetch the user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Dynamically create a user using get_user_model()
        user = User.objects.create_user(**validated_data)
        # Generate an authentication token for the user
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Define field for 'username'
    password = serializers.CharField()  # Define field for 'password'
