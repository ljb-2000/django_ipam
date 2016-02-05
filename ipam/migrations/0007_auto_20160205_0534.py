# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0006_auto_20151108_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subnet',
            name='environment',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
