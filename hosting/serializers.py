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
    hostingId = serializers.IntegerField(required=True)
    perNightCost = serializers.IntegerField()
    entirePrivateOrShared = serializers.CharField(max_length=20)
    highestGuestNo = serializers.IntegerField()
    beds = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    bathrooms = serializers.IntegerField()
    privateBathroomAvailable = serializers.IntegerField()
    needHostConfirmation = serializers.BooleanField()
    partialPayAllowed = serializers.BooleanField()
    categoryId = serializers.IntegerField()

    def create(self, validated_data):
        return Property.objects.create(
            hostingId=validated_data.get('hostingId'),
            perNightCost=validated_data.get('perNightCost'),
            entirePrivateOrShared=validated_data.get('entirePrivateOrShared'),
            highestGuestNo=validated_data.get('highestGuestNo'),
            beds=validated_data.get('beds'),
            bedrooms=validated_data.get('bedrooms'),
            bathrooms=validated_data.get('bathrooms'),
            privateBathroomAvailable=validated_data.get('privateBathroomAvailable'),
            needHostConfirmation=validated_data.get('needHostConfirmation'),
            partialPayAllowed=validated_data.get('partialPayAllowed'),
            categoryId=validated_data.get('categoryId'),
        )

    # def update(self, instance, validated_data):
    #     # Once the request data has been validated, we can update the todo item instance in the database
    #     print(instance.description)
    #     instance.text = validated_data.get('text', instance.text)
    #     print(instance.description)
    #     instance.save()
    #     return instance

    class Meta:
        model = Property
        fields = (
            'hostingId',
            'perNightCost',
            'EntirePrivateOrShared',
            'highestGuestNo',
            'beds',
            'bedrooms',
            'bathrooms',
            'privateBathroomAvailable',
            'needHostConfirmation',
            'partialPayAllowed',
            'categoryId'
        )
