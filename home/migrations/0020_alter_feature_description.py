# Generated by Django 5.1.6 on 2025-02-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_personalinfo_embedded_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.CharField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
