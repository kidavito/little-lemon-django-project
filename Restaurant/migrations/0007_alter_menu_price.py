# Generated by Django 4.1.7 on 2023-02-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0006_alter_booking_no_of_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
