# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extras.db.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0004_auto_20150104_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('identifier', models.CharField(null=True, max_length=200, blank=True)),
                ('is_source', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('REPR', 'Page'), ('SMPL', 'Sample'), ('SRCH', 'Search')], max_length=4, default='REPR')),
                ('artist', models.ForeignKey(related_name='links', to='happenings.Artist')),
                ('third_party', models.ForeignKey(to='happenings.ThirdParty')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('identifier', models.CharField(null=True, max_length=200, blank=True)),
                ('is_source', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('REPR', 'Page'), ('SMPL', 'Sample'), ('SRCH', 'Search')], max_length=4, default='REPR')),
                ('location', models.ForeignKey(related_name='links', to='happenings.Location')),
                ('third_party', models.ForeignKey(to='happenings.ThirdParty')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artist',
            name='third_parties',
            field=models.ManyToManyField(through='happenings.ArtistLink', to='happenings.ThirdParty'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='happeninglink',
            name='category',
            field=models.CharField(choices=[('REPR', 'Page'), ('SMPL', 'Sample'), ('SRCH', 'Search')], max_length=4, default='REPR'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='third_parties',
            field=models.ManyToManyField(through='happenings.LocationLink', to='happenings.ThirdParty'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='happening',
            name='artists',
            field=models.ManyToManyField(db_table='performance', to='happenings.Artist', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=django_extras.db.models.fields.LatitudeField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='lon',
            field=django_extras.db.models.fields.LongitudeField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)]),
            preserve_default=True,
        ),
    ]
