# Generated by Django 3.2.8 on 2021-11-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0006_auto_20211120_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]