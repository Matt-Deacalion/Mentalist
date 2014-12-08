# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('iteration', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LittlePrinter',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pearl',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('status', models.CharField(choices=[('question', 'question'), ('task', 'task'), ('fact', 'fact'), ('definition', 'definition'), ('image', 'image')], default='question', max_length=20)),
                ('text', models.CharField(blank=True, max_length=500)),
                ('answer', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('minutes', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='iteration',
            name='pearl',
            field=models.ForeignKey(to='core.Pearl'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iteration',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
