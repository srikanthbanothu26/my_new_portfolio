# Generated by Django 5.1.6 on 2025-02-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_projectinfo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='description',
            field=models.TextField(default=None, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='processstep',
            name='name',
            field=models.CharField(blank=True, null=True, verbose_name='Name'),
        ),
    ]
