# Generated by Django 4.1.7 on 2023-02-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0004_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guest',
            field=models.IntegerField(default=None),
        ),
    ]
