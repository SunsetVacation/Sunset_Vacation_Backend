from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view, renderer_classes
from .models import Categories
from django.core import serializers

# from .serializers import UserSerializer
from rest_framework import status
import json
import requests


@api_view(['GET'])
def getCategories(request):
    categories = Categories.objects.all().values_list('categoryName', flat=True).distinct()
    print(categories)
    return Response({'categories': categories, 'success': True},status=status.HTTP_200_OK)

@api_view(['POST'])
def getSubCategories(request):
    category = request.data["category"]
    subCategories = Categories.objects.filter(categoryName=category)
    return Response({'subcategories' : subCategories, 'success': True}, status=status.HTTP_200_OK)