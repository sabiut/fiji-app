# Generated by Django 3.1.1 on 2020-10-25 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fijiApi', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='villages',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village', to='fijiApi.provinces'),
        ),
    ]
