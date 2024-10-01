# Generated by Django 5.0.1 on 2024-02-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Nên nằm trong khoảng 155-160 kí tự', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Nên nằm trong khoảng 55-70 kí tự', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='Ví dụ: iphone-15-pro-max-16gb', max_length=255, null=True, unique=True),
        ),
    ]
