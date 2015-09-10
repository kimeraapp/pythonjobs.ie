# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_phone_and_external_not_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='token',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
