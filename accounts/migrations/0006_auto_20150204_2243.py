# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150204_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createuserteacher',
            name='teacher',
            field=models.CharField(max_length=100, verbose_name=b'Professor'),
            preserve_default=True,
        ),
    ]
