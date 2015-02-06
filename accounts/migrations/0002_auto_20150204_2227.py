# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0008_auto_20150204_2227'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='materia',
        ),
        migrations.AddField(
            model_name='materia',
            name='aluno',
            field=models.ForeignKey(default=1, to='students.Createstudent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='id_professor',
            field=models.ForeignKey(default=1, to='teachers.Createteacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='serie',
            field=models.CharField(default=1, max_length=30, verbose_name=b'Serie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='turno',
            field=models.CharField(default=1, max_length=20, verbose_name=b'Turno'),
            preserve_default=False,
        ),
    ]
