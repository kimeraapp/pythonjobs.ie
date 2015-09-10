# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_updated_the_initial_database_structure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='external_link',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='phone',
            field=models.CharField(max_length=15, blank=True),
        ),
    ]
