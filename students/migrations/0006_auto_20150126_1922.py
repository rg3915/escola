# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20150126_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createstudent',
            name='place_birth',
            field=models.CharField(max_length=20, verbose_name='Naturalidade', choices=[['S\xe3o Paulo', b'SP'], ['Bel\xe9m', b'PA'], ['Rio de Janeiro', b'RJ'], ['Goi\xe2nia', b'GO'], ['Salvador', b'BA'], ['Guarulhos', b'SP'], ['Bras\xedlia', b'DF'], ['Campinas', b'SP'], ['Fortaleza', b'CE'], ['S\xe3o Lu\xeds', b'MA'], ['Belo Horizonte', b'MG'], ['S\xe3o Gon\xe7alo', b'RJ'], ['Manaus', b'AM'], ['Macei\xf3', b'AL'], ['Curitiba', b'PR'], ['Duque de Caxias', b'RJ'], ['Recife', b'PE'], ['Natal', b'RN'], ['Porto Alegre', b'RS'], ['Campo Grande', b'MS']]),
            preserve_default=True,
        ),
    ]
