# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0002_auto_20151108_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='superblock',
            name='region',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
