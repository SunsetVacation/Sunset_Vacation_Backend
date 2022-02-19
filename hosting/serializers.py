from dataclasses import field, fields
from importlib.metadata import requires
# from typing_extensions import Required
from rest_framework import serializers
from .models import Category, Hosting, Property, Facility, Property_Facilities


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category_id', 'category_name', 'subcategory_name', 'description'
        )


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = (
            'facility_id', 'facility_name', 'facility_type'
        )


class HostingSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=500, required=False)
    max_days_refund = serializers.IntegerField(required=False)
    hosting_start_date = serializers.DateField(required=False)
    published = serializers.BooleanField(default=False)
    owner_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Hosting.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            max_days_refund=validated_data.get('max_days_refund'),
            hosting_start_date=validated_data.get('hosting_start_date'),
            published=validated_data.get('published'),
            owner_id=validated_data.get('owner_id')
        )

    def update(self, hosting, validated_data):
        hosting.title = validated_data.get('title') if validated_data.get('title') else hosting.title
        hosting.description = validated_data.get('description') if validated_data.get(
            'description') else hosting.description
        hosting.max_days_refund = validated_data.get('max_days_refund') if validated_data.get(
            'max_days_refund') else hosting.max_days_refund
        hosting.hosting_start_date = validated_data.get('hosting_start_date') if validated_data.get(
            'hosting_start_date') else hosting.hosting_start_date
        hosting.published = validated_data.get('published') if validated_data.get('published') else hosting.published
        hosting.save()
        return hosting

    class Meta:
        model = Hosting
        fields = (
            'hosting_id',
            'title',
            'description',
            'max_days_refund',
            'hosting_start_date',
            'published',
            'owner_id'
        )


class PropertySerializer(serializers.ModelSerializer):
    hosting_id = serializers.IntegerField(required=False)
    per_night_cost = serializers.IntegerField(required=False)
    entire_private_or_shared = serializers.CharField(max_length=20, required=False)
    highest_guest_no = serializers.IntegerField(required=False)
    beds = serializers.IntegerField(required=False)
    bedrooms = serializers.IntegerField(required=False)
    bathrooms = serializers.IntegerField(required=False)
    private_bathroom_available = serializers.IntegerField(required=False)
    need_host_confirmation = serializers.BooleanField(default=False)
    partial_pay_allowed = serializers.BooleanField(default=False)
    category_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Property.objects.create(
            hosting_id=validated_data.get('hosting_id'),
            per_night_cost=validated_data.get('per_night_cost'),
            entire_private_or_shared=validated_data.get('entire_private_or_shared'),
            highest_guest_no=validated_data.get('highest_guest_no'),
            beds=validated_data.get('beds'),
            bedrooms=validated_data.get('bedrooms'),
            bathrooms=validated_data.get('bathrooms'),
            private_bathroom_available=validated_data.get('private_bathroom_available'),
            need_host_confirmation=validated_data.get('need_host_confirmation'),
            partial_pay_allowed=validated_data.get('partial_pay_allowed'),
            category_id=validated_data.get('category_id'),
        )

    def update(self, property, validated_data):
        property.per_night_cost = validated_data.get('per_night_cost') if validated_data.get(
            'per_night_cost') else property.per_night_cost
        property.entire_private_or_shared = validated_data.get('entire_private_or_shared') if validated_data.get(
            'entire_private_or_shared') else property.entire_private_or_shared
        property.highest_guest_no = validated_data.get('highest_guest_no') if validated_data.get(
            'highest_guest_no') else property.highest_guest_no
        property.beds = validated_data.get('beds') if validated_data.get('beds') else property.beds
        property.bedrooms = validated_data.get('bedrooms') if validated_data.get('bedrooms') else property.bedrooms
        property.bathrooms = validated_data.get('bathrooms') if validated_data.get('bathrooms') else property.bathrooms
        property.private_bathroom_available = validated_data.get('private_bathroom_available') if validated_data.get(
            'private_bathroom_available') else property.private_bathroom_available
        property.need_host_confirmation = validated_data.get('need_host_confirmation') if validated_data.get(
            'need_host_confirmation') else property.need_host_confirmation
        property.partial_pay_allowed = validated_data.get('partial_pay_allowed') if validated_data.get(
            'partial_pay_allowed') else property.partial_pay_allowed
        property.category_id = validated_data.get('category_id') if validated_data.get(
            'category_id') else property.category_id
        property.save()
        return property

    class Meta:
        model = Property
        fields = (
            'hosting_id',
            'per_night_cost',
            'entire_private_or_shared',
            'highest_guest_no',
            'beds',
            'bedrooms',
            'bathrooms',
            'private_bathroom_available',
            'need_host_confirmation',
            'partial_pay_allowed',
            'category_id'
        )


# class PropertyFacilitiesSerializer(serializers.ModelSerializer):
#     property_facility_id = serializers.IntegerField(required=False)
#     hosting = serializers.IntegerField(required=False)
#     facility = serializers.IntegerField(required=False)

#     def create(self, validated_data):
#         return PropertyFacilities.objects.create(
#             property_facility_id=validated_data.get('property_facility_id'),
#             hosting=validated_data.get('hosting'),
#             facility=validated_data.get('facility')
#         )

#     def update(self, property_facilities, validated_data):
#         property_facilities.property_facility_id = validated_data.get('property_facility_id') if validated_data.get('property_facility_id') else  property_facilities.property_facility_id
#         property_facilities.hosting = validated_data.get('hosting') if validated_data.get('hosting') else property_facilities.hosting
#         property_facilities.facility = validated_data.get('facility') if validated_data.get('facility') else property_facilities.facility
#         property_facilities.save()
#         return property_facilities


#     class Meta:
#         model = PropertyFacilities
#         fields = (
#             "property_facility_id",
#             "hosting",
#             "facility"
#         )


class PropertyFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Facilities
        fields = (
            "hosting",
            "facility"
        )

