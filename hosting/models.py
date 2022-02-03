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
        default=None,
        null=True
    )

    hostingStartDate = models.DateField(
        default=None,
        null=True
    )

    published = models.BooleanField(
        default=False
    )

    owner = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )


class Property(models.Model):
    hosting = models.ForeignKey(
        Hosting,
        null=False,
        on_delete= models.CASCADE
    )

    perNightCost = models.IntegerField(
        default=None,
        null=True
    )

    entirePrivateOrShared = models.CharField(
        max_length=20,
        blank=False,
        null=True
    )

    highestGuestNo = models.IntegerField(
        default=None,
        null=True
    )

    beds = models.IntegerField(
        default=None,
        null=True
    )

    bedrooms = models.IntegerField(
        default=None,
        null=True
    )

    bathrooms = models.IntegerField(
        default=None,
        null=True
    )

    privateBathroomAvailable = models.IntegerField(
        default=None,
        null=True
    )

    needHostConfirmation = models.BooleanField(
        default=False
    )

    partialPayAllowed = models.BooleanField(
        default=False
    )

    category = models.ForeignKey(
        Category,
        null=False,
        on_delete=models.CASCADE
    )

