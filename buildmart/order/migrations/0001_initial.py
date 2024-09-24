# Generated by Django 5.1.1 on 2024-09-19 08:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homeowner', '0001_initial'),
        ('material', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(max_length=200)),
                ('cart_data', models.JSONField()),
                ('homeowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='homeowner.homeowner')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='material.material')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='supplier.supplier')),
            ],
        ),
    ]
