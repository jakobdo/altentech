# Generated by Django 3.0.7 on 2020-07-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_servicearea'),
        ('project', '0003_project_service_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='service_area',
            field=models.ManyToManyField(related_name='projects', to='tag.ServiceArea'),
        ),
    ]
