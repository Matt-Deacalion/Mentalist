# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141223_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pearl',
            name='status',
            field=models.CharField(max_length=20, choices=[('question', 'question'), ('task', 'task'), ('fact', 'fact'), ('quote', 'quote'), ('definition', 'definition'), ('image', 'image')], default='question'),
            preserve_default=True,
        ),
    ]
