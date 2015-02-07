# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20150206_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='falta',
            field=models.IntegerField(null=True, verbose_name=b'Falta', blank=True),
            preserve_default=True,
        ),
    ]
