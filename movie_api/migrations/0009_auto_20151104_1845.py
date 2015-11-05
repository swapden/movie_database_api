# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0008_auto_20151104_1843'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('movie', 'comment', 'owner')]),
        ),
    ]
