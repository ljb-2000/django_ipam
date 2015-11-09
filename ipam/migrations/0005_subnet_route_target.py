# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0004_subnet_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='subnet',
            name='route_target',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
