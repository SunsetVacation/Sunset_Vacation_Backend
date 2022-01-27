from rest_framework import serializers

from .models import  User


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
