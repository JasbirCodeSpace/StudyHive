# Generated by Django 3.2.8 on 2021-11-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0003_auto_20211111_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resource',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
