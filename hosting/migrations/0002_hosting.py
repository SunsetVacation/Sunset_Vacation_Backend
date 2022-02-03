# Generated by Django 4.0.1 on 2022-02-02 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_delete_hosting'),
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('hosting', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default=None, max_length=100, null=True)),
                ('description', models.CharField(default=None, max_length=500, null=True)),
                ('maxDaysRefund', models.IntegerField(default=None)),
                ('hostingStartDate', models.DateTimeField(default=None)),
                ('published', models.BooleanField(default=False)),
                ('ownerId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user')),
            ],
        ),
    ]