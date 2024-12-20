# Generated by Django 5.1.3 on 2024-11-23 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0002_citydistrict'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='city_district',
            field=models.ForeignKey(blank=True, help_text='The district where the event is taking place.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizers.citydistrict', verbose_name='City District'),
        ),
    ]
