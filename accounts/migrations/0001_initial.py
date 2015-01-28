# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20150126_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userstudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.ForeignKey(verbose_name=b'Nome', to='students.Createstudent')),
            ],
            options={
                'verbose_name': 'Conta estudante',
                'verbose_name_plural': 'Contas estudantes',
            },
            bases=(models.Model,),
        ),
    ]
