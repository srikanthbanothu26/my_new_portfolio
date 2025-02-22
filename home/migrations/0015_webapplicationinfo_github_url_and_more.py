# Generated by Django 5.1.6 on 2025-02-20 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_workexperienceinfo_company_workkeyresponsiblities'),
    ]

    operations = [
        migrations.AddField(
            model_name='webapplicationinfo',
            name='github_url',
            field=models.URLField(default=None, verbose_name='GitHub Repository'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_feature', to='home.projectinfo'),
        ),
        migrations.AlterField(
            model_name='webapplicationinfo',
            name='description',
            field=models.TextField(default=None, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='webapplicationinfo',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='webapplicationinfo',
            name='technologies',
            field=models.TextField(default=None, verbose_name='Technologies Used'),
        ),
    ]
