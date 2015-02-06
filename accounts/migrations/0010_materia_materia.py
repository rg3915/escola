# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_usermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='materia',
            field=models.CharField(default=1, max_length=20, verbose_name=b'Materia', choices=[(b'Matematica', b'Matematica'), (b'Portugues', b'Portugues'), (b'Geografia', b'Geografia'), (b'Ciencias', b'Ciencias'), (b'Ingles', b'Ingles')]),
            preserve_default=False,
        ),
    ]
