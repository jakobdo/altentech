# Generated by Django 3.0.7 on 2020-07-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_teaser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='teaser',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
