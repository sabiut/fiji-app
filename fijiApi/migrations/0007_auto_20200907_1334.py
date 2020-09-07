# Generated by Django 3.1.1 on 2020-09-07 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fijiApi', '0006_auto_20200907_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districts',
            name='confederancy',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district', to='fijiApi.confederacy'),
        ),
        migrations.AlterField(
            model_name='villages',
            name='confederancy',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village', to='fijiApi.confederacy'),
        ),
    ]
