# Generated by Django 4.0 on 2021-12-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_api', '0004_remove_vehicle_driver_vehicle_with_drivers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
