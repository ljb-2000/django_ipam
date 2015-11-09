# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subnet',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('address_space', models.CharField(max_length=255)),
                ('vrf', models.CharField(max_length=255, blank=True)),
                ('vlan_id', models.IntegerField()),
                ('environment', models.CharField(max_length=255)),
                ('customer_name', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuperBlock',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('address_space', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='subnet',
            name='super_block',
            field=models.ForeignKey(to='ipam.SuperBlock'),
        ),
    ]
