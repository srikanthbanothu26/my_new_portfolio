# Generated by Django 5.1.6 on 2025-02-20 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_certificateattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperienceinfo',
            name='company',
            field=models.CharField(blank=True, null=True, verbose_name='Company'),
        ),
        migrations.CreateModel(
            name='Workkeyresponsiblities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Name')),
                ('key_responsiblity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='key_responsiblity', to='home.workexperienceinfo')),
            ],
        ),
    ]
