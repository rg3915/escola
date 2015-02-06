# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20150204_2227'),
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
                ('student', models.ManyToManyField(related_name='aluno', to='students.Alunos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Createteacher',
            fields=[
                ('id_teacher', models.AutoField(serialize=False, primary_key=True)),
                ('teacher', models.CharField(max_length=200, verbose_name=b'Professor')),
                ('address', models.CharField(max_length=300, verbose_name='Endere\xe7o')),
                ('cep', models.IntegerField(max_length=8, verbose_name=b'CEP')),
                ('registry_mec', models.CharField(max_length=10, verbose_name='Registro mec')),
                ('graduation', models.CharField(max_length=150, verbose_name='Gradua\xe7\xe3o')),
                ('pos_graduation', models.CharField(unique=True, max_length=150, verbose_name='Pos Gradua\xe7\xe3o')),
                ('master_degree', models.CharField(unique=True, max_length=150, verbose_name=b'Mestrado')),
                ('doctorate', models.CharField(max_length=150, verbose_name=b'Doutorado')),
                ('birth_date', models.DateField(verbose_name=b'Data de nascimento')),
            ],
            options={
                'verbose_name': 'Cadastro professor',
                'verbose_name_plural': 'Cadastro professores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id_mat', models.AutoField(serialize=False, primary_key=True)),
                ('materia1', models.CharField(max_length=40, verbose_name='Materia 1', choices=[['Portugu\xeas', b'Portugu\xc3\xaas'], ['Matematica', b'Matematica'], ['Geografia', b'Geografia']])),
                ('materia2', models.CharField(blank=True, max_length=40, verbose_name=b'Materia 2', choices=[['Portugu\xeas', b'Portugu\xc3\xaas'], ['Matematica', b'Matematica'], ['Geografia', b'Geografia']])),
                ('materia3', models.CharField(blank=True, max_length=40, verbose_name=b'Materia 3', choices=[['Portugu\xeas', b'Portugu\xc3\xaas'], ['Matematica', b'Matematica'], ['Geografia', b'Geografia']])),
                ('materia4', models.CharField(blank=True, max_length=40, verbose_name=b'Materia 4', choices=[['Portugu\xeas', b'Portugu\xc3\xaas'], ['Matematica', b'Matematica'], ['Geografia', b'Geografia']])),
                ('materia5', models.CharField(blank=True, max_length=40, verbose_name=b'Materia 5', choices=[['Portugu\xeas', b'Portugu\xc3\xaas'], ['Matematica', b'Matematica'], ['Geografia', b'Geografia']])),
                ('prof', models.ForeignKey(verbose_name=b'Professor', to='teachers.Createteacher', max_length=200)),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
            bases=(models.Model,),
        ),
    ]
