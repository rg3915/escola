# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20150126_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('aluno_id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=120)),
                ('serie', models.IntegerField()),
                ('turno', models.CharField(max_length=120)),
                ('idade', models.IntegerField()),
                ('nota', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
            bases=(models.Model,),
        ),
    ]
