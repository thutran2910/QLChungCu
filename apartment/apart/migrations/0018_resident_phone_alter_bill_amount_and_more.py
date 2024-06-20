# Generated by Django 4.2.11 on 2024-06-20 12:30

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart', '0017_remove_survey_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='resident',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
