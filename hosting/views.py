from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import api_view, renderer_classes
from core.models import User
from .models import Category, Hosting, Property, Facility, Property_Facilities, Location, Property_Images
from .serializers import CategorySerializer, HostingSerializer, PropertySerializer, FacilitySerializer, LocationSerializer, PropertyFacilitiesSerializer, PropertyImagesSerializer
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
    return Response({'facilities': facilities_serializer.data, 'success': True}, status=status.HTTP_200_OK)


class PropertyHostingView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin,
):
    def post(self, request):
        print(request.data)
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
            print(property_serializer.errors)
            print(property_serializer.error_messages)
            hosting.delete()
            return Response({"error": "Property creation error"}, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        location_serializer = LocationSerializer(data=request.data)
        if location_serializer.is_valid():
            location = location_serializer.save()
            location_serializer = LocationSerializer(location)
        else:
            print(location_serializer.errors)
            print(location_serializer.error_messages)
            hosting.delete()
            property.delete()
            return Response({"error": "Location creation error"}, status=status.HTTP_404_NOT_FOUND)
        facilities = request.data["facilities"]
        print(facilities)
        for id in facilities:
            try:
                facility = Facility.objects.get(facility_id=id)
                new_prop_facility = Property_Facilities(hosting=hosting, facility=facility)
                new_prop_facility.save()
            except Facility.DoesNotExist:
                return Response({"error": "No facility to store"}, status=status.HTTP_404_NOT_FOUND)

        images = request.data["images"]
        print(request.data['images'])
        for image in images:
            try:
                new_prop_image = Property_Images(hosting=hosting, link=image["src"])
                new_prop_image.save()
            except Property_Images.DoesNotExist:
                return Response({"error": "No facility to store"}, status=status.HTTP_404_NOT_FOUND)
        facilities = Property_Facilities.objects.all().filter(hosting_id=hosting.hosting_id)
        facilities_serializer = PropertyFacilitiesSerializer(facilities, many=True)
        images = Property_Images.objects.all().filter(hosting_id=hosting.hosting_id)
        images_serializer = PropertyImagesSerializer(images, many=True)
        return Response({"hosting": hosting_serializer.data, "property": property_serializer.data, "location": location_serializer.data, "facilities": facilities_serializer.data, "images": images_serializer.data},
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

        try:
            location = Location.objects.get(hosting_id=hosting_id)
        except Location.DoesNotExist:
            return Response({'errors': 'This location does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        location_serializer = LocationSerializer(location, data=request.data)
        if location_serializer.is_valid():
            location = location_serializer.save()
            location_serializer = LocationSerializer(location)
        else:
            print(location_serializer.errors)
            print(location_serializer.error_messages)
            return Response({'errors': 'location update failed'}, status=status.HTTP_400_BAD_REQUEST)

        keys = []
        for key in request.data.keys():
            keys.append(key)

        if "facilities" in keys:
            old_facilities = Property_Facilities.objects.all().filter(hosting_id=hosting_id)
            old_facilities.delete()
            facilities = request.data["facilities"]
            print(facilities)
            for id in facilities:
                try:
                    facility = Facility.objects.get(facility_id=id)
                    new_prop_facility = Property_Facilities(hosting=hosting, facility=facility)
                    new_prop_facility.save()
                except Facility.DoesNotExist:
                    return Response({"error": "No facility to store"}, status=status.HTTP_404_NOT_FOUND)

        if "images" in keys:
            old_images = Property_Images.objects.all().filter(hosting_id=hosting_id)
            old_images.delete()
            images = request.data["images"]
            print(request.data['images'])
            for image in images:
                try:
                    new_prop_image = Property_Images(hosting=hosting, link=image["src"])
                    new_prop_image.save()
                except Property_Images.DoesNotExist:
                    return Response({"error": "No facility to store"}, status=status.HTTP_404_NOT_FOUND)
        facilities = Property_Facilities.objects.all().filter(hosting_id=hosting.hosting_id)
        facilities_serializer = PropertyFacilitiesSerializer(facilities, many=True)
        images = Property_Images.objects.all().filter(hosting_id=hosting.hosting_id)
        images_serializer = PropertyImagesSerializer(images, many=True)
        return Response({"hosting": hosting_serializer.data, "property": property_serializer.data, "location": location_serializer.data, "facilities": facilities_serializer.data, "images": images_serializer.data},
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
        images = Property_Images.objects.all().filter(hosting_id=hosting_id)
        images.delete()
        facilities = Property_Facilities.objects.all().filter(hosting_id=hosting_id)
        facilities.delete()
        location = Location.objects.get(hosting_id=hosting_id)
        location.delete()
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
