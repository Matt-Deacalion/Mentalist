# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20141216_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oauth',
            options={'verbose_name_plural': 'OAuths'},
        ),
        migrations.RemoveField(
            model_name='iteration',
            name='user',
        ),
        migrations.AddField(
            model_name='pearl',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
