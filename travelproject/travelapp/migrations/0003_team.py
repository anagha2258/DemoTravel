# Generated by Django 5.0.2 on 2024-02-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_rename_des_place_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=250)),
                ('t_img', models.ImageField(upload_to='pics')),
                ('t_desc', models.TextField()),
            ],
        ),
    ]
