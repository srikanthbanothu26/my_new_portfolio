# Generated by Django 5.1.6 on 2025-02-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_personalinfo_twitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='embedded_location',
            field=models.CharField(blank=True, verbose_name='Embedded Location'),
        ),
    ]
