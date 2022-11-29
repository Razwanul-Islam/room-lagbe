# Generated by Django 3.2.13 on 2022-11-27 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_featuredhotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(blank=True, choices=[('single', 'single'), ('double', 'double')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='RoomBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]