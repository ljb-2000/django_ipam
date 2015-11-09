# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0003_superblock_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='subnet',
            name='region',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
