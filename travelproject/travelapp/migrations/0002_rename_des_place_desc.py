# Generated by Django 5.0.2 on 2024-02-19 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='des',
            new_name='desc',
        ),
    ]
