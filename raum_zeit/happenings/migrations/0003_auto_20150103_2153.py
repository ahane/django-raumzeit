# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0002_auto_20150102_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='HappeningLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('url', models.URLField()),
                ('happening', models.ForeignKey(to='happenings.Happening')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('is_source', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='happeninglink',
            name='third_party',
            field=models.ForeignKey(to='happenings.ThirdParty'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='artist',
            name='links',
        ),
        migrations.RemoveField(
            model_name='happening',
            name='links',
        ),
        migrations.RemoveField(
            model_name='location',
            name='links',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.AddField(
            model_name='happening',
            name='third_parties',
            field=models.ManyToManyField(through='happenings.HappeningLink', to='happenings.ThirdParty'),
            preserve_default=True,
        ),
    ]
