# Generated by Django 3.2.8 on 2021-11-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others'), ('N', 'Prefer not to say')], max_length=50, null=True),
        ),
    ]
