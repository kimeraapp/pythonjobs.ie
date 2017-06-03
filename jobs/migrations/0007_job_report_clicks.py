# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_token_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='report_clicks',
            field=models.IntegerField(default=0),
        ),
    ]
