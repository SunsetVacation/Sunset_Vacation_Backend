from django.db import models


class User(models.model):
    userId = models.AutoField(
        primary_key=True
    )

    firstName = models.CharField(
        max_length=100,
        allow_blank=False,
        allow_null=False,
        trim_whitespace=True
    )

    lastName = models.CharField(
        max_length=100,
        allow_blank=False,
        allow_null=False,
        trim_whitespace=True
    )

    email = models.EmailField(
        max_length=50,
        allow_blank=false,
        allow_null=True,
        unique=True
    )

    phoneNo = models.CharField(
        max_length=20,
        allow_blank=False,
        allow_null=True,
        trim_whitespace=True
    )

    host = models.BooleanField(
        default=False
    )

    addressId = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL
    )


class Profile(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    name = models.TextField(
        max_length=30,
        null=False,
        blank=False
    )
