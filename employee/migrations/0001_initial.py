# Generated by Django 3.0.7 on 2020-06-04 11:15

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('jobtitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', stdimage.models.JPEGField(upload_to='employee')),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField(choices=[(None, '(Unknown)'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')])),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technology.Technology')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='technologies',
            field=models.ManyToManyField(through='employee.TechnologyLevel', to='technology.Technology'),
        ),
    ]
