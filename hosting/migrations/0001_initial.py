# Generated by Django 4.0.1 on 2022-02-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(default=None, max_length=100, null=True)),
                ('subCategoryName', models.CharField(default=None, max_length=100, null=True)),
                ('description', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
    ]