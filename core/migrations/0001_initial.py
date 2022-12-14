# Generated by Django 3.2.13 on 2022-11-14 16:09

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('description', tinymce.models.HTMLField()),
                ('location', models.CharField(max_length=300)),
                ('cover_photo', models.ImageField(upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room_number', models.CharField(max_length=50)),
                ('room_type', models.CharField(blank=True, max_length=50, null=True)),
                ('is_booked', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hotel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
