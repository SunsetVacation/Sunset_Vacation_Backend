from django.db import models


class Address(models.Model):
    address_id = models.AutoField(
        primary_key=True
    )

    house_no = models.IntegerField(
        default=None,
    )

    city = models.CharField(
        max_length=45,
        default=None,
        blank=False,
        null=True
    )

    zipcode = models.IntegerField(
        default=None,
    )

    country = models.CharField(
        max_length=45,
        default=None,
        blank=False,
        null=True
    )


class User(models.Model):
    user_id = models.AutoField(
        primary_key=True
    )

    firstname = models.CharField(
        max_length=100,
        default=None,
        blank=False,
        null=True
    )

    lastname = models.CharField(
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

    phone_no = models.CharField(
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


