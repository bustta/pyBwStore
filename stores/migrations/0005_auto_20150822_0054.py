# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_city_name_in_cht'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
