# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0012_auto_20150115_2121'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='performance',
            unique_together=set([('happening', 'artist')]),
        ),
    ]
