# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_materia_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='falta',
            field=models.IntegerField(default=1, verbose_name=b'Falta', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='nota',
            field=models.DecimalField(default=2, verbose_name=b'Nota', max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
