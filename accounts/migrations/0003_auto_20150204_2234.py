# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150204_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createuserteacher',
            name='materia',
        ),
        migrations.AlterField(
            model_name='materia',
            name='id_professor',
            field=models.ForeignKey(to='accounts.CreateUserTeacher'),
            preserve_default=True,
        ),
    ]
