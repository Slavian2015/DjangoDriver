# Generated by Django 4.0 on 2021-12-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_api', '0005_alter_driver_created_at_alter_vehicle_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateField(default='14.12.2021'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created_at',
            field=models.DateField(default='14.12.2021'),
        ),
    ]