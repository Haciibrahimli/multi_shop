# Generated by Django 5.0 on 2024-01-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0017_maindetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='maindetails',
            name='locations',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='locations'),
        ),
    ]
