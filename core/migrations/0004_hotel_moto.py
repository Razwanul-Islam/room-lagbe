# Generated by Django 3.2.13 on 2022-11-28 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221127_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='moto',
            field=models.TextField(default='Catchy moto goes here...', null=True),
        ),
    ]
