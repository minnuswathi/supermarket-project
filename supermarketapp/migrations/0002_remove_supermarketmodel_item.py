# Generated by Django 3.2.5 on 2021-09-21 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supermarketapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supermarketmodel',
            name='item',
        ),
    ]
