# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Createstudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Nome')),
                ('last_name', models.CharField(max_length=250, verbose_name=b'Sobre nome')),
                ('sex', models.CharField(max_length=9, verbose_name=b'Sexo', choices=[[b'Masculino', b'M'], [b'Feminino', b'F']])),
                ('mother_name', models.CharField(max_length=250, verbose_name='Nome da m\xe3e')),
                ('father_name', models.CharField(max_length=250, verbose_name='Nome do pai')),
                ('address', models.CharField(max_length=300, verbose_name='Endere\xe7o')),
                ('district', models.CharField(max_length=100, verbose_name=b'Bairro')),
                ('cep', models.IntegerField(max_length=8, verbose_name=b'CEP')),
                ('inscription', models.SmallIntegerField(unique=True, max_length=50, verbose_name='Inscri\xe7\xe3o')),
                ('birth_date', models.DateField(verbose_name='Data de nascimento')),
                ('place_birth', models.CharField(max_length=20, verbose_name='Naturalidade', choices=[['S\xe3o Paulo', b'SP'], ['Bel\xe9m', b'PA'], ['Rio de Janeiro', b'RJ'], ['Goi\xe2nia', b'GO'], ['Salvador', b'BA'], ['Guarulhos', b'SP'], ['Bras\xedlia', b'DF'], ['Campinas', b'SP'], ['Fortaleza', b'CE'], ['S\xe3o Lu\xeds', b'MA'], ['Belo Horizonte', b'MG'], ['S\xe3o Gon\xe7alo', b'RJ'], ['Manaus', b'AM'], ['Macei\xf3', b'AL'], ['Curitiba', b'PR'], ['Duque de Caxias', b'RJ'], ['Recife', b'PE'], ['Natal', b'RN'], ['Porto Alegre', b'RS'], ['Campo Grande', b'MS']])),
                ('nationality', models.CharField(max_length=20, verbose_name=b'Nacionalidade')),
                ('other', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Cadastro aluno',
                'verbose_name_plural': 'Cadastro alunos',
            },
            bases=(models.Model,),
        ),
    ]
