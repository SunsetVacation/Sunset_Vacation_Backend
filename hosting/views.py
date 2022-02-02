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
    try:
        categories = Categories.objects.all().values_list('categoryName', flat=True).distinct()
    except Categories.DoesNotExist:
        return Response({"error": "No category to show"}, status=status.HTTP_404_NOT_FOUND)
    return Response({'categories': categories, 'success': True}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getSubCategories(request):
    category = request.data["category"]
    print(category)
    try:
        sub_categories = Categories.objects.get(categoryName=category)
    except Categories.DoesNotExist:
        return Response({"error": "No subcategory to show"}, status=status.HTTP_404_NOT_FOUND)
    return Response({'subcategories': sub_categories, 'success': True}, status=status.HTTP_200_OK)
