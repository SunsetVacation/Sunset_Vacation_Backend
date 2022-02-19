from operator import truediv
from tkinter.tix import Tree
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import User, Address, PhotoUpload
from hosting.models import Hosting
# from .serializers import UserSerializer
from rest_framework import status
import json
import requests

from .serializers import PhotoUploadSerializer


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
        return Response({"user": user.user_id, "host": user.host, "unpublishedHosting": False, "success": True},
                        status=status.HTTP_200_OK)
    try:
        Hosting.objects.get(owner=user, published=False)
    except Hosting.DoesNotExist:
        return Response({"user": user.user_id, "host": user.host, "unpublishedHosting": False, "success": True})
    return Response({"user": user.user_id, "host": user.host, "unpublishedHosting": True, "success": True},
                    status=status.HTTP_200_OK)


# class PhotoUploadView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         photos = PhotoUpload.objects.all()
#         serializer = PhotoUploadSerializer(photos, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs): 
#         print(request.data)
#         return Response({"hello": "hello", "success": True}, status=status.HTTP_201_CREATED)
# photos_serializer = PhotoUploadSerializer(data=request.data)
# photo = request.FILES['']
# if photos_serializer.is_valid():
#     photos_serializer.save()
#     return Response({"uploaded_photo":photos_serializer.data, "success": True}, status=status.HTTP_201_CREATED)
# else:
#     print('error', photos_serializer.errors)
#     return Response(photos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def photoUpload(request):
    print(request.data)
    photos_serializer = PhotoUploadSerializer(data=request.data)
    if photos_serializer.is_valid():
        photos_serializer.save()
        return Response({"uploaded_photo": photos_serializer.data, "success": True}, status=status.HTTP_201_CREATED)
    else:
        print('error', photos_serializer.errors)
        return Response({"error": photos_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    # return Response({"hello": "hello", "success": True})
