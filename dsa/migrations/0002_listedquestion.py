# Generated by Django 3.2.8 on 2021-11-12 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dsa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListedQuestion',
            fields=[
                ('date', models.DateTimeField(auto_now_add=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dsa.question')),
            ],
            options={
                'verbose_name': 'ListedQuestion',
                'verbose_name_plural': 'ListedQuestions',
            },
        ),
    ]
