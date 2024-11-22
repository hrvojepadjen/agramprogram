# Generated by Django 5.1.3 on 2024-11-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(blank=True, help_text='The location where the event will be held.', null=True, verbose_name='Location'),
        ),
    ]