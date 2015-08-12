# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20150810_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name_in_cht',
            field=models.CharField(default=datetime.datetime(2015, 8, 12, 14, 12, 25, 903968, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
