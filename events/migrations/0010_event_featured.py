# Generated by Django 5.1.3 on 2024-11-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_event_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured',
            field=models.BooleanField(default=False, help_text='Indicates whether this event is featured.', verbose_name='Featured Event'),
        ),
    ]
