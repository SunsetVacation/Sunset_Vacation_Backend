from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view, renderer_classes
from .models import Profile, User
from .serializers import ProfileSerializer, UserSerializer
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
    user_serializer = UserSerializer(user)
    return Response({"user": user_serializer.data}, status=status.HTTP_200_OK)


class ProfileListView(
    APIView,  # Basic View class provided by the Django Rest Framework
    UpdateModelMixin,  # Mixin that allows the basic APIView to handle PUT HTTP requests
    DestroyModelMixin,  # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
            # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                # Check if the todo item the user wants to update exists
                queryset = Profile.objects.get(id=id)
            except Profile.DoesNotExist:
                # If the todo item does not exist, return an error response
                return Response({'errors': 'This profile item does not exist.'}, status=400)

            # Serialize todo item from Django queryset object to JSON formatted data
            read_serializer = ProfileSerializer(queryset)

        else:
            # Get all todo items from the database using Django's model ORM
            queryset = Profile.objects.all()

            # Serialize list of todos item from Django queryset object to JSON formatted data
            read_serializer = ProfileSerializer(queryset, many=True)

            # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)
