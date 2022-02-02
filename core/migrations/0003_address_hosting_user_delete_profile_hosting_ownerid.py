# Generated by Django 4.0.1 on 2022-01-31 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_id_alter_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressId', models.AutoField(primary_key=True, serialize=False)),
                ('houseNo', models.IntegerField(default=None)),
                ('city', models.CharField(default=None, max_length=45, null=True)),
                ('zipCode', models.IntegerField(default=None)),
                ('country', models.CharField(default=None, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('hosting', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default=None, max_length=100, null=True)),
                ('description', models.CharField(default=None, max_length=500, null=True)),
                ('maxDaysRefund', models.IntegerField(default=None)),
                ('hostingStartDate', models.DateTimeField(default=None)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(default=None, max_length=100, null=True)),
                ('lastName', models.CharField(default=None, max_length=100, null=True)),
                ('email', models.EmailField(default=None, max_length=50, null=True, unique=True)),
                ('phoneNo', models.CharField(default=None, max_length=20, null=True)),
                ('host', models.BooleanField(default=False)),
                ('password', models.CharField(default=None, max_length=500, null=True)),
                ('addressId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.address')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='hosting',
            name='ownerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user'),
        ),
    ]
