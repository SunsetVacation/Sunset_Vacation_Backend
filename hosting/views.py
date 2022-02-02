from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view, renderer_classes
from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets
from django.core import serializers
from rest_framework.decorators import action

# from .serializers import UserSerializer
from rest_framework import status
import json
import requests


@api_view(['GET'])
def getCategories(request):
    try:
        categories = Category.objects.all().values_list('categoryName', flat=True).distinct()
    except Category.DoesNotExist:
        return Response({"error": "No category to show"}, status=status.HTTP_404_NOT_FOUND)
    return Response({'categories': categories, 'success': True}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getSubCategories(request):
    category = request.data["category"]
    print(category)
    try:
        sub_categories = Category.objects.all().filter(categoryName=category)
    except Category.DoesNotExist:
        return Response({"error": "No subcategory to show"}, status=status.HTTP_404_NOT_FOUND)
    sub_categories = CategorySerializer(sub_categories, many=True)
    return Response({'subcategories': sub_categories.data, 'success': True}, status=status.HTTP_200_OK)


# class CategoryViewSet(viewsets.ModelViewSet):
#     category_serializer = CategorySerializer
#
#     @action(methods=['GET'], detail=True, url_path='categories')
#     def getCategories(self, request):
#         try:
#             categories = Category.objects.all().values_list('categoryName', flat=True).distinct()
#         except Category.DoesNotExist:
#             return Response({"error": "No category to show"}, status=status.HTTP_404_NOT_FOUND)
#         return Response({'categories': categories, 'success': True}, status=status.HTTP_200_OK)


