from rest_framework import serializers
from .models import Category, Hosting, Property


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'categoryId', 'categoryName', 'subCategoryName', 'description'
        )


class HostingSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100,required=True)
    description = serializers.CharField(max_length=500)
    maxDaysRefund = serializers.IntegerField()
    hostingStartDate = serializers.DateTimeField()
    published = serializers.BooleanField()
    ownerId = serializers.IntegerField(required=True)

    def create(self, validated_data):
        # Once the request data has been validated, we can create a todo item instance in the database
        return Hosting.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            maxDaysRefund=validated_data.get('maxDaysRefund'),
            hostingStartDate=validated_data.get('hostingStartDate'),
            published=validated_data.get('published'),
            ownerId=validated_data.get('ownerId')
        )

    # def update(self, instance, validated_data):
    #     # Once the request data has been validated, we can update the todo item instance in the database
    #     print(instance.description)
    #     instance.text = validated_data.get('text', instance.text)
    #     print(instance.description)
    #     instance.save()
    #     return instance

    class Meta:
        model = Hosting
        fields = (
            'hostingId',
            'title',
            'description',
            'maxDaysRefund',
            'hostingStartDate',
            'published',
            'ownerId'
        )


# class PropertySerializer(serializers.ModelSerializer):
#     hostingId = serializers.IntegerField(required=True)
#     perNightCost = serializers.IntegerField()
#     entirePrivateOrShared = serializers.CharField(max_length=20)
#     highestGuestNo = serializers.IntegerField()
#     beds = serializers.IntegerField()
#     bedrooms = serializers.IntegerField()
#     bathrooms = serializers.IntegerField()
#     privateBathroomAvailable = serializers.IntegerField()
#     needHostConfirmation = serializers.BooleanField()
#     partialPayAllowed = serializers.BooleanField()
#     categoryId = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Property.objects.create(
#             hostingId=validated_data.get('hostingId'),
#             perNightCost=validated_data.get('perNightCost'),
#             entirePrivateOrShared=validated_data.get('entirePrivateOrShared'),
#             highestGuestNo=validated_data.get('highestGuestNo'),
#             beds=validated_data.get('beds'),
#             bedrooms=validated_data.get('bedrooms'),
#             bathrooms=validated_data.get('bathrooms'),
#             privateBathroomAvailable=validated_data.get('privateBathroomAvailable'),
#             needHostConfirmation=validated_data.get('needHostConfirmation'),
#             partialPayAllowed=validated_data.get('partialPayAllowed'),
#             categoryId=validated_data.get('categoryId'),
#         )

    # def update(self, instance, validated_data):
    #     # Once the request data has been validated, we can update the todo item instance in the database
    #     print(instance.description)
    #     instance.text = validated_data.get('text', instance.text)
    #     print(instance.description)
    #     instance.save()
    #     return instance

    # class Meta:
    #     model = Hosting
    #     fields = (
    #         'hostingId',
    #         'perNightCost',
    #         'EntirePrivateOrShared',
    #         'highestGuestNo',
    #         'beds',
    #         'bedrooms',
    #         'bathrooms',
    #         'privateBathroomAvailable',
    #         'needHostConfirmation',
    #         'partialPayAllowed',
    #         'categoryId'
    #     )
