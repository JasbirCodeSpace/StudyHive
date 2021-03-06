# Generated by Django 3.2.8 on 2021-11-11 16:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import resource.models.resource


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211102_1804'),
        ('resource', '0002_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Q', 'Question paper'), ('N', 'Notes'), ('B', 'Book')], max_length=1)),
                ('file', models.FileField(upload_to=resource.models.resource.get_upload_path)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource.subject')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
    ]
