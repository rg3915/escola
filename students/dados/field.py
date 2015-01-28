# -*- encoding: utf-8 -*-
"""
List of choices for districts, horario, series and sex.
"""



DISTRICT_CHOICES = [
    [u'São Paulo', 'SP'],
    [u'Belém', 'PA'],
    [u'Rio de Janeiro', 'RJ'],
    [u'Goiânia', 'GO'],
    [u'Salvador', 'BA'],
    [u'Guarulhos', 'SP'],
    [u'Brasília', 'DF'],
    [u'Campinas', 'SP'],
    [u'Fortaleza', 'CE'],
    [u'São Luís', 'MA'],
    [u'Belo Horizonte', 'MG'],
    [u'São Gonçalo', 'RJ'],
    [u'Manaus', 'AM'],
    [u'Maceió', 'AL'],
    [u'Curitiba', 'PR'],
    [u'Duque de Caxias', 'RJ'],
    [u'Recife', 'PE'],
    [u'Natal', 'RN'],
    [u'Porto Alegre', 'RS'],
    [u'Campo Grande', 'MS']]

"""
(

	("AC", "Acre"),
	("AL", "Alagoas"),
	("AP", "Amapá"),
	("AM", "Amazonas"),
	("BH", "Bahia"),
	("CE", "Ceará"),
	("ES", "Espírito Santo"),
	("Goiás", "GO"),
	("MR", "Maranhão"),
	("MT", "Mato Grosso"),
	("MTS", "Mato Grosso do Sul"),
	("MG", "Minas Gerais"),
	("PA", "Pará"),
	("PB", "Paraíba"),
	("PR", "Paraná"),
	("", "Pernambuco"),
	("", "Piauí"),
	("", "Rio de Janeiro"),
	("", "Rio Grande do Norte"),
	("", "Rio Grande do Sul"),
	("", "Rondônia"),
	("", "Roraima"),
	("", "Santa Catarina"),
	("", "São Paulo"),
	("", "Sergipe"),
	("", "Tocantins")
)
"""


HORARIO_CHOICES = (
	("MATUTINO", "MATUTINO"),
	("VESPERTINO", "VESPERTINO"),
	("NOTURNO", "NOTURNO")

)


SERIES_CHOICES = (
	("CA", "1º ano"),
	("1ª série", "2° ano"),
	("2ª série", "3° ano"),
	("3ª série", "4° ano"),
	("4ª série", "5° ano"),
	("5ª série", "6° ano"),
	("6ª série", "7° ano"),
	("7ª série", "8° ano"),
	("8ª série", "9° ano")

) # CA = Classe de Alfabetização

SEX_CHOICES = [
	['M', 'Masculino'],
	['F', 'Feminino']
]
