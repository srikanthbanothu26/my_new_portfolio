# Generated by Django 5.1.6 on 2025-02-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_personalinfo_embedded_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='embedded_location',
            field=models.TextField(blank=True, verbose_name='Embedded Location'),
        ),
    ]
