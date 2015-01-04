# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Happening',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('titel', models.CharField(max_length=200)),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
