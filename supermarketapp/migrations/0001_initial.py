# Generated by Django 3.2.5 on 2021-09-21 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupermarketModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_mobile', models.CharField(max_length=10)),
                ('customer_address', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarketapp.items')),
            ],
        ),
    ]