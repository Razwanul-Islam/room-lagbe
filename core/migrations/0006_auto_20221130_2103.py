# Generated by Django 3.2.13 on 2022-11-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20221128_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='per_night_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='roombook',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='roombook',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('booked', 'booked'), ('checked_in', 'checked_in'), ('checked_out', 'checked_out'), ('cancelled', 'cancelled')], max_length=50),
        ),
    ]