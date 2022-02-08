from rest_framework import serializers
from .models import Category, Hosting, Property, Facility


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
    class Meta:
        model = Hosting
        fields = (
            'hosting_id',
            'title',
            'description',
            'max_days_refund',
            'hosting_start_date',
            'published',
            'owner'
        )


class PropertySerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     return Property.objects.create(
    #         hostingId=validated_data.get('hostingId'),
    #         perNightCost=validated_data.get('perNightCost'),
    #         entirePrivateOrShared=validated_data.get('entirePrivateOrShared'),
    #         highestGuestNo=validated_data.get('highestGuestNo'),
    #         beds=validated_data.get('beds'),
    #         bedrooms=validated_data.get('bedrooms'),
    #         bathrooms=validated_data.get('bathrooms'),
    #         privateBathroomAvailable=validated_data.get('privateBathroomAvailable'),
    #         needHostConfirmation=validated_data.get('needHostConfirmation'),
    #         partialPayAllowed=validated_data.get('partialPayAllowed'),
    #         categoryId=validated_data.get('categoryId'),
    #     )

    class Meta:
        model = Property
        fields = (
            'hosting',
            'per_night_cost',
            'entire_private_or_shared',
            'highest_guest_no',
            'beds',
            'bedrooms',
            'bathrooms',
            'private_bathroom_available',
            'need_host_confirmation',
            'partial_pay_allowed',
            'category'
        )
