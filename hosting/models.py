from django.db import models
from core.models import User


# Create your models here.


class Categories(models.Model):
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
    hosting = models.AutoField(
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
