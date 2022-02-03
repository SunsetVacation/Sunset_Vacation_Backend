from django.db import models


class Address(models.Model):
    addressId = models.AutoField(
        primary_key=True
    )

    houseNo = models.IntegerField(
        default=None,
    )

    city = models.CharField(
        max_length=45,
        default=None,
        blank=False,
        null=True
    )

    zipCode = models.IntegerField(
        default=None,
    )

    country = models.CharField(
        max_length=45,
        default=None,
        blank=False,
        null=True
    )


class User(models.Model):
    userId = models.AutoField(
        primary_key=True
    )

    firstName = models.CharField(
        max_length=100,
        default=None,
        blank=False,
        null=True
    )

    lastName = models.CharField(
        max_length=100,
        default=None,
        blank=False,
        null=True
    )

    email = models.EmailField(
        max_length=50,
        default=None,
        blank=False,
        null=True,
        unique=True
    )

    phoneNo = models.CharField(
        max_length=20,
        default=None,
        blank=False,
        null=True
    )

    host = models.BooleanField(
        default=False
    )

    password = models.CharField(
        max_length=500,
        default=None,
        blank=False,
        null=True
    )

    address = models.ForeignKey(
        Address,
        null=True,
        on_delete=models.SET_NULL
    )


