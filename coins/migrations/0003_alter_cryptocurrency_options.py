# Generated by Django 3.2.11 on 2022-01-15 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_cryptocurrency_full_updated_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cryptocurrency',
            options={'managed': False},
        ),
    ]