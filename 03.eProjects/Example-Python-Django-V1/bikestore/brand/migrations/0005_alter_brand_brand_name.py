# Generated by Django 5.0.1 on 2024-02-27 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_alter_brand_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
