# Generated by Django 3.1.1 on 2020-09-20 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fijiApi', '0007_auto_20200907_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
