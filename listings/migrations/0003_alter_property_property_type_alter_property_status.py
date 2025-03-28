# Generated by Django 5.1.6 on 2025-02-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_property_image_property_property_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('commercial', 'Commercial')], default='house', max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('rented', 'Rented'), ('sold', 'Sold')], default='available', max_length=50),
        ),
    ]
