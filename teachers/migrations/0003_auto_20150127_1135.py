# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20150127_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias',
            name='prof',
            field=models.ForeignKey(verbose_name=b'Professor', to='teachers.Createteacher', max_length=200),
            preserve_default=True,
        ),
    ]
