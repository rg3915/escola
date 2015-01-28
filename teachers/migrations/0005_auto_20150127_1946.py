# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_anotations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotations',
            name='student',
            field=models.ManyToManyField(to='students.Alunos', verbose_name=b'Aluno'),
            preserve_default=True,
        ),
    ]
