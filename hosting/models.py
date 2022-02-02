from django.db import models

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