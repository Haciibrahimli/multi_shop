# Generated by Django 4.2.5 on 2024-01-04 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_comment_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partniors',
            name='slug',
        ),
    ]
