# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUserTeacher',
            fields=[
                ('id_teacher', models.AutoField(serialize=False, primary_key=True)),
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
                ('materia', models.CharField(max_length=20, verbose_name=b'Materia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='createuserteacher',
            name='materia',
            field=models.ManyToManyField(to='accounts.Materia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='createuserteacher',
            name='teacher',
            field=models.ForeignKey(verbose_name=b'Professor', to='accounts.UserModel'),
            preserve_default=True,
        ),
    ]
