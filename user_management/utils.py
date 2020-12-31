from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise  serializers.ValidationError("Invalid credentials. Please try again")
    return user

def create_user_account(email, password, first_name="",
                        last_name="", **extra_fields):
    user = User.objects.create_user(
        username=email, email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)
    return user