# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materias',
            old_name='id_prof',
            new_name='id_mat',
        ),
    ]
