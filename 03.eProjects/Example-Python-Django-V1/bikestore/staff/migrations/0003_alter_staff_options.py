# Generated by Django 5.0.1 on 2024-02-26 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_staff_options_alter_staff_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['-id', 'first_name']},
        ),
    ]