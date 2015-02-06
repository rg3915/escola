# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150204_2234'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anotations',
            name='student',
        ),
        migrations.DeleteModel(
            name='Anotations',
        ),
        migrations.RemoveField(
            model_name='materias',
            name='prof',
        ),
        migrations.DeleteModel(
            name='Createteacher',
        ),
        migrations.DeleteModel(
            name='Materias',
        ),
    ]
