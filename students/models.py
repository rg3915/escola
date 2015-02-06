# coding: utf-8
from django.db import models
from .dados.field import *
#from .dados.fields import *



class Createstudent(models.Model):
	name = models.CharField(verbose_name = u'Nome', max_length=250, blank=False) # nome
	last_name = models.CharField(verbose_name = u'Sobre nome', max_length=250, blank=False) # sobre nome
	sex = models.CharField(verbose_name = u'Sexo', max_length=9, choices= SEX_CHOICES, blank=False) # sexo
	mother_name = models.CharField(verbose_name = u'Nome da mãe', max_length=250, blank=False) # nome da mãe
	father_name = models.CharField(verbose_name = u'Nome do pai', max_length=250, blank=False) # nome do pai
	address = models.CharField(verbose_name = u'Endereço', max_length=300, blank=False) # endereço
	district = models.CharField(verbose_name = u'Bairro', max_length=100, blank=False) # bairro
	cep = models.IntegerField(verbose_name = u'CEP', max_length=8, blank=False) # CEP
	inscription = models.SmallIntegerField(verbose_name = u'Inscrição', max_length=50, unique=True, blank=False) # inscrição
	birth_date = models.DateField(verbose_name = u'Data de nascimento', blank=False) # data de nascimento
	place_birth = models.CharField(verbose_name = u'Naturalidade', max_length=20, choices= DISTRICT_CHOICES, blank=False) # naturalidade
	nationality = models.CharField(verbose_name=u'Nacionalidade', max_length=20, blank=False) # nacionalidade

	
	class Meta:
		verbose_name = u"Cadastro aluno"
		verbose_name_plural = u"Cadastro alunos"

	def __unicode__(self):
		return self.name + " " + self.last_name


class Alunos(models.Model):
	aluno_id = models.AutoField(primary_key=True, unique=True)
	nome = models.ForeignKey(Createstudent, max_length=120)
	serie = models.IntegerField()
	turno = models.CharField(max_length=120)
	nota = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		verbose_name='Aluno'
		verbose_name_plural='Alunos'

	def __unicode__(self):

		return self.nome