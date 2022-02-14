from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view, renderer_classes
from core.models import User
from .models import Category, Hosting, Property, Facility
from .serializers import CategorySerializer, HostingSerializer, PropertySerializer, FacilitySerializer
from rest_framework import viewsets
from django.core import serializers
from rest_framework.decorators import action

from rest_framework import status
import json
import requests


@api_view(['GET'])
def getCategories(request):
    try:
        categories = Category.objects.all().values_list('category_name', flat=True).distinct()
    except Category.DoesNotExist:
        return Response({"error": "No category to show"}, status=status.HTTP_404_NOT_FOUND)
    return Response({'categories': categories, 'success': True}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getSubcategories(request, category=None, *arg, **kwargs):
    # category = request.data["category"]
    try:
        subcategories = Category.objects.all().filter(category_name=category)
    except Category.DoesNotExist:
        return Response({"error": "No subcategory to show"}, status=status.HTTP_404_NOT_FOUND)
    subcategories_serializer = CategorySerializer(subcategories, many=True)
    return Response({'subcategories': subcategories_serializer.data, 'success': True}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getFacilities(request):
    try:
        facilities = Facility.objects.all()
    except Facility.DoesNotExist:
        return Response({"error": "No facility to show"}, status=status.HTTP_404_NOT_FOUND)
    facilities_serializer = FacilitySerializer(facilities, many=True)
    return Response({'facilities': facilities_serializer.data}, status=status.HTTP_200_OK)


class PropertyHostingView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin,
):
    def post(self, request):
        hosting_serializer = HostingSerializer(data=request.data)
        if hosting_serializer.is_valid():
            hosting = hosting_serializer.save()
            hosting_serializer = HostingSerializer(hosting)
        else:
            return Response({"error": "Hosting creation error"}, status=status.HTTP_400_BAD_REQUEST)
        request.data["hosting_id"] = hosting.hosting_id
        property_serializer = PropertySerializer(data=request.data)
        if property_serializer.is_valid():
            property = property_serializer.save()
            property_serializer = PropertySerializer(property)
        else:
            hosting.delete()
            return Response({"error": "Property creation error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"hosting": hosting_serializer.data, "property": property_serializer.data},
                        status=status.HTTP_201_CREATED)

    def put(self, request, hosting_id=None, *args, **kwargs):
        try:
            hosting = Hosting.objects.get(hosting_id=hosting_id)
        except Hosting.DoesNotExist:
            return Response({'errors': 'This hosting does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        hosting_serializer = HostingSerializer(hosting, data=request.data)
        if hosting_serializer.is_valid():
            hosting = hosting_serializer.save()
            hosting_serializer = HostingSerializer(hosting)
        else:
            return Response({'errors': 'Hosting update failed'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            property = Property.objects.get(hosting_id=hosting_id)
        except Property.DoesNotExist:
            return Response({'errors': 'This property does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        property_serializer = PropertySerializer(property, data=request.data)
        if property_serializer.is_valid():
            property = property_serializer.save()
            property_serializer = PropertySerializer(property)
        else:
            print(property_serializer.errors)
            print(property_serializer.error_messages)
            return Response({'errors': 'Property update failed'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"hosting": hosting_serializer.data, "property": property_serializer.data},
                        status=status.HTTP_200_OK)

    def get(self, request, hosting_id=None, *args, **kwargs):
        if hosting_id:
            try:
                property = Property.objects.get(hosting_id=hosting_id)
            except Property.DoesNotExist:
                return Response({'errors': 'This property does not exist.'}, status=400)
            property_serializer = PropertySerializer(property)
            try:
                hosting = Hosting.objects.get(hosting_id=hosting_id)
            except Hosting.DoesNotExist:
                return Response({'errors': 'This hosting does not exist.'}, status=400)
            hosting_serializer = HostingSerializer(hosting)
            return Response({"hosting": hosting_serializer.data, "property": property_serializer.data},
                            status=status.HTTP_200_OK)
        else:
            try:
                property = Property.objects.all()
            except Property.DoesNotExist:
                return Response({'errors': 'This property does not exist.'}, status=400)
            property_serializer = PropertySerializer(property, many=True)
            try:
                hosting = Hosting.objects.all()
            except Hosting.DoesNotExist:
                return Response({'errors': 'This hosting does not exist.'}, status=400)
            hosting_serializer = HostingSerializer(hosting, many=True)
            return Response({"hosting": hosting_serializer.data, "property": property_serializer.data},
                            status=status.HTTP_200_OK)

    def delete(self, request, hosting_id=None, *args, **kwargs):
        try:
            property = Property.objects.get(hosting_id=hosting_id)
        except Property.DoesNotExist:
            return Response({'errors': 'This property does not exist.'}, status=400)

        property.delete()

        try:
            hosting = Hosting.objects.get(hosting_id=hosting_id)
        except Hosting.DoesNotExist:
            return Response({'errors': 'This hosting does not exist.'}, status=400)

        hosting.delete()

        return Response(status=status.HTTP_200_OK)
