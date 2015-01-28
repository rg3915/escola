# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150126_2325'),
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
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('endereco', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
