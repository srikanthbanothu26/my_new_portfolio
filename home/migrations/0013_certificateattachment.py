# Generated by Django 5.1.6 on 2025-02-20 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_feature_description_processstep_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='certificates/')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='home.certificateinfo')),
            ],
        ),
    ]
