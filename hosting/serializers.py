from rest_framework import serializers
from .models import Category, Hosting, Property


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'categoryId', 'categoryName', 'subCategoryName', 'description'
        )


class HostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hosting
        fields = (
            'hostingId',
            'title',
            'description',
            'maxDaysRefund',
            'hostingStartDate',
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
            'perNightCost',
            'EntirePrivateOrShared',
            'highestGuestNo',
            'beds',
            'bedrooms',
            'bathrooms',
            'privateBathroomAvailable',
            'needHostConfirmation',
            'partialPayAllowed',
            'category'
        )
