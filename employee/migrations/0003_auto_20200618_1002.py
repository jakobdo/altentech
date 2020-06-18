# Generated by Django 3.0.7 on 2020-06-18 08:02

import django.core.validators
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='cv',
            field=models.FileField(null=True, upload_to='cv/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=stdimage.models.JPEGField(upload_to='employee/'),
        ),
    ]
