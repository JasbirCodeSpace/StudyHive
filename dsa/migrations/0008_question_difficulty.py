# Generated by Django 3.2.8 on 2021-11-20 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0007_auto_20211120_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default='E', max_length=1),
        ),
    ]
