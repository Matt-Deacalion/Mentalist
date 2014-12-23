# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141217_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pearl',
            name='text',
            field=models.TextField(blank=True, max_length=500),
            preserve_default=True,
        ),
    ]
