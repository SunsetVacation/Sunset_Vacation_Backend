# Generated by Django 4.0.1 on 2022-02-02 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_address_hosting_user_delete_profile_hosting_ownerid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hosting',
        ),
    ]