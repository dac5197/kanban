# Generated by Django 3.1.5 on 2021-01-16 18:49

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210116_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='number',
            field=models.CharField(default=core.models.increment_board_number, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(default=core.models.increment_card_number, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='lane',
            name='number',
            field=models.CharField(default=core.models.increment_lane_number, max_length=20, unique=True),
        ),
    ]
