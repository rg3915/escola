# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alunos'),
        ('teachers', '0003_auto_20150127_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anotations',
            fields=[
                ('id_Ano', models.AutoField(serialize=False, primary_key=True)),
                ('not1', models.IntegerField(max_length=10, verbose_name=b'Nota 1')),
                ('not2', models.IntegerField(max_length=10, verbose_name=b'Nota 2')),
                ('not3', models.IntegerField(max_length=10, verbose_name=b'Nota 3')),
                ('not4', models.IntegerField(max_length=10, verbose_name=b'Nota 4')),
                ('student', models.ManyToManyField(to='students.Alunos', max_length=200, verbose_name=b'Aluno')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
