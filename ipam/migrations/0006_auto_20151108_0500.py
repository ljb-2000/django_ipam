# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0005_subnet_route_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superblock',
            name='address_space',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
