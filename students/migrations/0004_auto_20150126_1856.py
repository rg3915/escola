# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_createstudent_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createstudent',
            name='place_birth',
            field=models.CharField(max_length=20, verbose_name='Naturalidade', choices=[(b'AC', b'Acrel\xc3\xa2ndia'), (b'AC', b'Assis Brasil'), (b'AC', b'Brasil\xc3\xa9ia'), (b'AC', b'Bujari'), (b'AC', b'Capixaba'), (b'AC', b'Cruzeiro do Sul'), (b'AC', b'Epitaciol\xc3\xa2ndia'), (b'AC', b'Feij\xc3\xb3'), (b'AC', b'Jord\xc3\xa3o'), (b'AC', b'M\xc3\xa2ncio Lima'), (b'AC', b'Manoel Urbano'), (b'AC', b'Marechal Thaumaturgo'), (b'AC', b'Pl\xc3\xa1cido de Castro'), (b'AC', b'Porto Acre'), (b'AC', b'Porto Walter'), (b'AC', b'Rio Branco'), (b'AC', b'Rodrigues Alves'), (b'AC', b'Santa Rosa do Purus'), (b'AC', b'Sena Madureira'), (b'AC', b'Senador Guiomard'), (b'AC', b'Tarauac\xc3\xa1'), (b'AC', b'Xapuri')]),
            preserve_default=True,
        ),
    ]
