# Generated by Django 3.2.8 on 2021-11-20 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0004_auto_20211120_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='likes',
        ),
    ]