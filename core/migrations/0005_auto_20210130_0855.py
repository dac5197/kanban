# Generated by Django 3.1.5 on 2021-01-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_card_lane_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lane',
            name='path',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
