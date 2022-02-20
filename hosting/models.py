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
        default=None,
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
        null=True,
        on_delete=models.CASCADE
    )


class Facility(models.Model):
    facility_id = models.AutoField(
        primary_key=True
    )

    facility_name = models.CharField(
        max_length=45,
        default=None,
        blank=False,
        null=True
    )

    facility_type = models.CharField(
        max_length=45,
        default=None,
        blank=False,
        null=True
    )

class PropertyFacilities(models.Model):
    hosting = models.ForeignKey(
        Hosting,
        on_delete=models.CASCADE,
        null=False
    )

    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        null=False
    )

# class Location(models.Model):
#     hosting = models.ForeignKey(
#         Hosting,
#         null=False,
#         on_delete=models.CASCADE,
#         primary_key=True
#     )
#     latitude = models.FloatField(
#         default=None,
#         null=True
#     )
#     longitude = models.FloatField(
#         default=None,
#         null=True
#     )

#     address = models.CharField(
#         max_length=200,
#         default=None,
#         blank=False,
#         null=True
#     )


# class Image(models.Model):
#     image_id = models.AutoField(
#         primary_key=True
#     )

#     hosting = models.ForeignKey(
#         Hosting,
#         null=False,
#         on_delete=models.CASCADE,
#     )

#     image_url = models.CharField(
#         max_length=500,
#         default=None,
#         blank=False,
#         null=True
#     )




class Property_Facilities(models.Model):
    hosting = models.ForeignKey(
        Hosting,
        on_delete=models.CASCADE,
        null=False
    )

    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        null=False
    )


class Location(models.Model):
    location_id = models.AutoField(
        primary_key=True
    )

    hosting = models.ForeignKey(
        Hosting,
        on_delete=models.CASCADE,
        null=False
    )

    longitude = models.FloatField(
        default=None,
        null=True
    )

    latitude = models.FloatField(
        default=None,
        null=True
    )

    address = models.CharField(
        max_length=200,
        default=None,
        blank=False,
        null=True
    )


class Property_Images(models.Model):
    hosting = models.ForeignKey(
        Hosting,
        on_delete=models.CASCADE,
        null=False
    )

    link = models.CharField(
        default=None,
        null=True,
        max_length=300
    )