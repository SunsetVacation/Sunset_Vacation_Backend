from django.db import models
from core.models import User


# Create your models here.


class Category(models.Model):
    categoryId = models.AutoField(
        primary_key=True
    )

    categoryName = models.CharField(
        max_length=100,
        default=None,
        blank=False,
        null=True
    )

    subCategoryName = models.CharField(
        max_length=100,
        default=None,
        blank=False,
        null=True
    )

    description = models.CharField(
        max_length=200,
        default=None,
        blank=False,
        null=True
    )


class Hosting(models.Model):
    hostingId = models.AutoField(
        primary_key=True
    )

    title = models.CharField(
        max_length=100,
        default=None,
        blank=False,
        null=True
    )

    description = models.CharField(
        max_length=500,
        default=None,
        blank=False,
        null=True
    )

    maxDaysRefund = models.IntegerField(
        default=None
    )

    hostingStartDate = models.DateTimeField(
        default=None
    )

    published = models.BooleanField(
        default=False
    )

    ownerId = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )


class Property(models.Model):
    hostingId = models.ForeignKey(
        Hosting,
        null=False,
        on_delete= models.CASCADE
    )

    perNightCost = models.IntegerField(
        default=None
    )

    entirePrivateOrShared = models.CharField(
        max_length=20,
        default=None,
        blank=False,
        null=True
    )

    highestGuestNo = models.IntegerField(
        default=None
    )

    beds = models.IntegerField(
        default=None
    )

    bedrooms = models.IntegerField(
        default=None
    )

    bathrooms = models.IntegerField(
        default=None
    )

    privateBathroomAvailable = models.IntegerField(
        default=None
    )

    needHostConfirmation = models.BooleanField(
        default=False
    )

    partialPayAllowed = models.BooleanField(
        default=False
    )

    categoryId = models.ForeignKey(
        Category,
        null=False,
        on_delete=models.CASCADE
    )

