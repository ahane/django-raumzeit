# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0005_auto_20150105_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance2',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('kind', models.CharField(default='DJ', choices=[('LIVE', 'Live Music'), ('LIDJ', 'Live Set'), ('DJ', 'Set')], max_length=4)),
                ('artist', models.ForeignKey(to='happenings.Artist', related_name='performances')),
                ('happening', models.ForeignKey(to='happenings.Happening', related_name='performances')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='happening',
            name='artists2',
            field=models.ManyToManyField(to='happenings.Artist', blank=True, through='happenings.Performance2', related_name='Happening2'),
            preserve_default=True,
        ),
    ]
