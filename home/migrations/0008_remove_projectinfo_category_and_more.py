# Generated by Django 5.1.6 on 2025-02-20 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_category_category_technology_technology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectinfo',
            name='category',
        ),
        migrations.RemoveField(
            model_name='projectinfo',
            name='features',
        ),
        migrations.RemoveField(
            model_name='projectinfo',
            name='technologies',
        ),
    ]
