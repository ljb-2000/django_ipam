# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0007_auto_20160205_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subnet',
            name='vlan_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
