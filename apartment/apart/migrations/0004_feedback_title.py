# Generated by Django 4.2.11 on 2024-05-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart', '0003_remove_flat_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='title',
            field=models.CharField(default='Mất điện', max_length=70),
        ),
    ]
