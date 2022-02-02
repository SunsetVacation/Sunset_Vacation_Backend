from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view, renderer_classes
from .models import User, Address
from hosting.models import Hosting
# from .serializers import UserSerializer
from rest_framework import status
import json
import requests


@api_view(['POST'])
def login(request):
    """Return a message"""
    email = request.data["email"]
    password = request.data["password"]
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "No user exists with provided user email"}, status=status.HTTP_404_NOT_FOUND)
    if user.password != password:
        return Response({"error": "Password did not match"}, status=status.HTTP_401_UNAUTHORIZED)
    if not user.host:
        return Response({"user": user.userId, "host": user.host, "unpublishedHosting": False, "success": True}, status=status.HTTP_200_OK)
    try:
        Hosting.objects.get(ownerId=user.userId, published=False)
    except Hosting.DoesNotExist:
        return Response({"user": user.userId, "host": user.host, "unpublishedHosting": False, "success": True})
    return Response({"user": user.userId, "host": user.host, "unpublishedHosting": True, "success": True}, status=status.HTTP_200_OK)
