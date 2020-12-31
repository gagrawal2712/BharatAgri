from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers

from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)
    
class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()
    
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'auth_token')
        read_only_fields = ('id', 'is_active', 'is_staff')
        
    
    def get_auth_token(self,  obj):
        token = Token.objects.filter(user=obj).first()
        if token is None:
            token = Token.objects.create(user=obj)
        return token.key

class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

class EmptySerializer(serializers.Serializer):
    pass
