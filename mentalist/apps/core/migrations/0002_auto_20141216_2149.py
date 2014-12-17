# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuth',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('client_key', models.CharField(max_length=50)),
                ('client_secret', models.CharField(max_length=50)),
                ('resource_owner_key', models.CharField(max_length=50)),
                ('resource_owner_secret', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='littleprinter',
            name='credentials',
            field=models.ForeignKey(to='core.OAuth', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='littleprinter',
            name='subscription_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
