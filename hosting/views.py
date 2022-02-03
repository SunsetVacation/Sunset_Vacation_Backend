from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view, renderer_classes
from core.models import User
from .models import Category, Hosting
from .serializers import CategorySerializer, HostingSerializer, PropertySerializer
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

class PropertyHostingView(
    APIView,  # Basic View class provided by the Django Rest Framework
    UpdateModelMixin,  # Mixin that allows the basic APIView to handle PUT HTTP requests
    DestroyModelMixin,  # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    # def post(self, request):
    #     try:
    #         # user = User.objects.get(userId=request.data.get('ownerId'))
    #         hosting = Hosting.objects.create(title=request.data.get('title'),
    #                                          description=request.data.get('description'),
    #                                          maxDaysRefund=request.data.get('maxDaysRefund'),
    #                                          hostingStartDate=request.data.get('hostingStartDate'),
    #                                          published=(True if request.data.get('published') is True else False),
    #                                          owner_id=request.data.get('owner'))
    #     except Hosting.DoesNotExist:
    #         Response({"error": "Hosting creation error"}, status=status.HTTP_400_BAD_REQUEST)
    #     hosting_serializer = HostingSerializer(hosting)
    #     return Response(hosting_serializer.data, status=status.HTTP_201_CREATED)



