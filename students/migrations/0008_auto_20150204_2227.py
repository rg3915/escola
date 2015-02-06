# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alunos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alunos',
            name='idade',
        ),
        migrations.AlterField(
            model_name='alunos',
            name='nome',
            field=models.ForeignKey(to='students.Createstudent', max_length=120),
            preserve_default=True,
        ),
    ]
