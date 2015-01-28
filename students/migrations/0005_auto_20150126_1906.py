# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20150126_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createstudent',
            name='place_birth',
            field=models.CharField(max_length=20, verbose_name='Naturalidade', choices=[(b'AC', b'Acrel\xc3\xa2ndia'), (b'AC', b'Assis Brasil'), (b'AC', b'Brasil\xc3\xa9ia'), (b'AC', b'Bujari'), (b'AC', b'Capixaba'), (b'AC', b'Cruzeiro do Sul'), (b'AC', b'Epitaciol\xc3\xa2ndia'), (b'AC', b'Feij\xc3\xb3'), (b'AC', b'Jord\xc3\xa3o'), (b'AC', b'M\xc3\xa2ncio Lima'), (b'AC', b'Manoel Urbano'), (b'AC', b'Marechal Thaumaturgo'), (b'AC', b'Pl\xc3\xa1cido de Castro'), (b'AC', b'Porto Acre'), (b'AC', b'Porto Walter'), (b'AC', b'Rio Branco'), (b'AC', b'Rodrigues Alves'), (b'AC', b'Santa Rosa do Purus'), (b'AC', b'Sena Madureira'), (b'AC', b'Senador Guiomard'), (b'AC', b'Tarauac\xc3\xa1'), (b'AC', b'Xapuri'), (b'AL', b'\xc3\x81gua Branca'), (b'AL', b'Anadia'), (b'AL', b'Arapiraca'), (b'AL', b'Atalaia'), (b'AL', b'Barra de Santo Ant\xc3\xb4nio'), (b'AL', b'Barra de S\xc3\xa3o Miguel'), (b'AL', b'Batalha'), (b'AL', b'Bel\xc3\xa9m'), (b'AL', b'Belo Monte'), (b'AL', b'Boca da Mata'), (b'AL', b'Branquinha'), (b'AL', b'Cacimbinhas'), (b'AL', b'Cajueiro'), (b'AL', b'Campestre'), (b'AL', b'Campo Alegre'), (b'AL', b'Campo Grande'), (b'AL', b'Canapi'), (b'AL', b'Capela'), (b'AL', b'Carneiros'), (b'AL', b'Ch\xc3\xa3 Preta'), (b'AL', b'Coit\xc3\xa9 do N\xc3\xb3ia'), (b'AL', b'Col\xc3\xb4nia Leopoldina'), (b'AL', b'Coqueiro Seco'), (b'AL', b'Coruripe'), (b'AL', b'Cra\xc3\xadbas'), (b'AL', b'Delmiro Gouveia'), (b'AL', b'Dois Riachos'), (b'AL', b'Estrela de Alagoas'), (b'AL', b'Feira Grande'), (b'AL', b'Feliz Deserto'), (b'AL', b'Flexeiras'), (b'AL', b'Girau do Ponciano'), (b'AL', b'Ibateguara'), (b'AL', b'Igaci'), (b'AL', b'Igreja Nova'), (b'AL', b'Inhapi'), (b'AL', b'Jacar\xc3\xa9 dos Homens'), (b'AL', b'Jacu\xc3\xadpe'), (b'AL', b'Japaratinga'), (b'AL', b'Jaramataia'), (b'AL', b'Joaquim Gomes'), (b'AL', b'Jundi\xc3\xa1'), (b'AL', b'Junqueiro'), (b'AL', b'Lagoa da Canoa'), (b'AL', b'Limoeiro de Anadia'), (b'AL', b'Macei\xc3\xb3'), (b'AL', b'Major Isidoro'), (b'AL', b'Mar Vermelho'), (b'AL', b'Maragogi'), (b'AL', b'Maravilha'), (b'AL', b'Marechal Deodoro'), (b'AL', b'Maribondo'), (b'AL', b'Mata Grande'), (b'AL', b'Matriz de Camaragibe'), (b'AL', b'Messias'), (b'AL', b'Minador do Negr\xc3\xa3o'), (b'AL', b'Monteir\xc3\xb3polis'), (b'AL', b'Murici'), (b'AL', b'Novo Lino'), (b'AL', b'Olho d`\xc3\x81gua das Flores'), (b'AL', b'Olho d`\xc3\x81gua do Casado'), (b'AL', b'Olho d`\xc3\x81gua Grande'), (b'AL', b'Oliven\xc3\xa7a'), (b'AL', b'Ouro Branco'), (b'AL', b'Palestina'), (b'AL', b'Palmeira dos \xc3\x8dndios'), (b'AL', b'P\xc3\xa3o de A\xc3\xa7\xc3\xbacar'), (b'AL', b'Pariconha'), (b'AL', b'Paripueira'), (b'AL', b'Passo de Camaragibe'), (b'AL', b'Paulo Jacinto'), (b'AL', b'Penedo'), (b'AL', b'Pia\xc3\xa7abu\xc3\xa7u'), (b'AL', b'Pilar'), (b'AL', b'Pindoba'), (b'AL', b'Piranhas'), (b'AL', b'Po\xc3\xa7o das Trincheiras'), (b'AL', b'Porto Calvo'), (b'AL', b'Porto de Pedras'), (b'AL', b'Porto Real do Col\xc3\xa9gio'), (b'AL', b'Quebrangulo'), (b'AL', b'Rio Largo'), (b'AL', b'Roteiro'), (b'AL', b'Santa Luzia do Norte'), (b'AL', b'Santana do Ipanema'), (b'AL', b'Santana do Munda\xc3\xba'), (b'AL', b'S\xc3\xa3o Br\xc3\xa1s'), (b'AL', b'S\xc3\xa3o Jos\xc3\xa9 da Laje'), (b'AL', b'S\xc3\xa3o Jos\xc3\xa9 da Tapera'), (b'AL', b'S\xc3\xa3o Lu\xc3\xads do Quitunde'), (b'AL', b'S\xc3\xa3o Miguel dos Campos'), (b'AL', b'S\xc3\xa3o Miguel dos Milagres'), (b'AL', b'S\xc3\xa3o Sebasti\xc3\xa3o'), (b'AL', b'Satuba'), (b'AL', b'Senador Rui Palmeira'), (b'AL', b'Tanque d`Arca'), (b'AL', b'Taquarana'), (b'AL', b'Teot\xc3\xb4nio Vilela'), (b'AL', b'Traipu'), (b'AL', b'Uni\xc3\xa3o dos Palmares'), (b'AL', b'Vi\xc3\xa7osa')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='createstudent',
            name='sex',
            field=models.CharField(max_length=9, verbose_name=b'Sexo', choices=[[b'M', b'Masculino'], [b'F', b'Feminino']]),
            preserve_default=True,
        ),
    ]
