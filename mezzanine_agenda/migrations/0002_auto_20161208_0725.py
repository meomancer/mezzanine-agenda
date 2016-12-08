# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title_af',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
    ]
