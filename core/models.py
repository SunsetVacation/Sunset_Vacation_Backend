from django.db import models


class Profile(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    name = models.TextField(
        max_length=30,
        null=False,
        blank=False
    )
