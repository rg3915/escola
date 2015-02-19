# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0008_auto_20150204_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampoMateria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=20, verbose_name='Turno')),
                ('serie', models.CharField(max_length=30, verbose_name='Serie')),
                ('nota', models.DecimalField(verbose_name=b'Nota', max_digits=10, decimal_places=2)),
                ('falta', models.IntegerField(null=True, verbose_name=b'Falta', blank=True)),
                ('aluno', models.ForeignKey(to='students.Createstudent')),
            ],
            options={
                'verbose_name': 'Campo Materia',
                'verbose_name_plural': 'Campos das Materias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampoProf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Campo_materia', models.ForeignKey(to='accounts.CampoMateria')),
                ('id_professor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Campo Professor',
                'verbose_name_plural': 'Campos dos Professores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreateUserTeacher',
            fields=[
                ('id_teacher', models.AutoField(serialize=False, primary_key=True)),
                ('teacher', models.CharField(max_length=100, verbose_name=b'Professor')),
            ],
            options={
                'verbose_name': 'Cadastro de professor',
                'verbose_name_plural': 'Cadastro de professores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('materia', models.CharField(max_length=40, verbose_name=b'Materia')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=200, verbose_name=b'User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campomateria',
            name='materia',
            field=models.ForeignKey(verbose_name=b'Materia', to='accounts.Materia'),
            preserve_default=True,
        ),
    ]
