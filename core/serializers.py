from rest_framework import serializers

from .models import Profile, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'userId',
            'firstName',
            'lastName',
            'email',
            'phoneNo',
            'host',
            'password',
            'addressId'
        )


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30, required=True)

    def create(self, validated_data):
        # Once the request data has been validated, we can create a todo item instance in the database
        return Profile.objects.create(
            name=validated_data.get('name')
        )

    def update(self, instance, validated_data):
        # Once the request data has been validated, we can update the todo item instance in the database
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = (
            'id',
            'name',
        )
