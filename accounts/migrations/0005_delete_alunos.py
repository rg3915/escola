# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_pessoa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Alunos',
        ),
    ]
