# Generated by Django 3.0.7 on 2020-07-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20200702_1033'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='consultants',
            field=models.ManyToManyField(related_name='projects', to='employee.Employee'),
        ),
    ]
