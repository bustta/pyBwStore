# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_auto_20150822_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='lng',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
