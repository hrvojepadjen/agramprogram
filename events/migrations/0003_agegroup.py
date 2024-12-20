# Generated by Django 5.1.3 on 2024-11-22 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the age group.', max_length=255, verbose_name='Age Group Name')),
            ],
            options={
                'verbose_name': 'Age Group',
                'verbose_name_plural': 'Age Groups',
            },
        ),
    ]
