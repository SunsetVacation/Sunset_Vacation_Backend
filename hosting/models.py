from django.db import models
from core.models import User


# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(
        primary_key=True
    )

    category_name = models.CharField(
        max_length=100,
        default=None,
        blank=False,
        null=True
    )

    subcategory_name = models.CharField(
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
    hosting_id = models.AutoField(
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

    max_days_refund = models.IntegerField(
        default=None,
        null=True
    )

    hosting_start_date = models.DateField(
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
        on_delete=models.CASCADE,
        primary_key=True
    )

    per_night_cost = models.IntegerField(
        default=None,
        null=True
    )

    entire_private_or_shared = models.CharField(
        max_length=20,
        blank=False,
        null=True
    )

    highest_guest_no = models.IntegerField(
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

    private_bathroom_available = models.IntegerField(
        default=None,
        null=True
    )

    need_host_confirmation = models.BooleanField(
        default=False
    )

    partial_pay_allowed = models.BooleanField(
        default=False
    )

    category = models.ForeignKey(
        Category,
        null=False,
        on_delete=models.CASCADE
    )

