# Generated by Django 4.2.11 on 2024-05-11 07:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apart', '0014_alter_resident_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
