# coding: utf-8
from django.db import models
from dados.list import *
from students.models import Alunos



class Createteacher(models.Model):
	id_teacher = models.AutoField(primary_key=True)
	teacher = models.CharField(verbose_name = 'Professor', max_length=200, blank=False)
	address = models.CharField(verbose_name = u'Endereço', max_length=300, blank=False)
	cep = models.IntegerField(verbose_name = 'CEP', max_length=8, blank=False)
	registry_mec = models.CharField(verbose_name = u'Registro mec', max_length=10, blank=False)
	graduation = models.CharField(verbose_name = u'Graduação', max_length=150, blank=False)
	pos_graduation = models.CharField(verbose_name = u'Pos Graduação', max_length=150, unique=True, blank=False)
	master_degree = models.CharField(verbose_name = 'Mestrado', max_length=150, unique=True, blank=False)
	doctorate = models.CharField(verbose_name = 'Doutorado', max_length=150, blank=False)
	birth_date = models.DateField(verbose_name='Data de nascimento', blank=False)

	class Meta:
		verbose_name = "Cadastro professor"
		verbose_name_plural = "Cadastro professores"

	def __unicode__(self):
		return self.teacher

class Materias(models.Model):
	id_mat = models.AutoField(primary_key=True)
	prof = models.ForeignKey(Createteacher, max_length=200, verbose_name='Professor')
	materia1 = models.CharField(max_length=40, verbose_name=u'Materia 1', choices =MAT_CHOICES, blank=False)
	materia2 = models.CharField(max_length=40, verbose_name='Materia 2', choices=MAT_CHOICES, blank=True)
	materia3 = models.CharField(max_length=40, verbose_name='Materia 3', choices=MAT_CHOICES, blank=True)
	materia4 = models.CharField(max_length=40, verbose_name='Materia 4', choices=MAT_CHOICES, blank=True)
	materia5 = models.CharField(max_length=40, verbose_name='Materia 5', choices=MAT_CHOICES, blank=True)
	
	class Meta:
		verbose_name='Materia'
		verbose_name_plural='Materias'

	def __unicode__(self):
		return u'%s' % self.prof


class Anotations(models.Model):
	id_Ano = models.AutoField(primary_key=True)
	student = models.ManyToManyField(Alunos, related_name='aluno')
	not1 = models.IntegerField(verbose_name='Nota 1', max_length=10, blank=False)
	not2 = models.IntegerField(verbose_name='Nota 2', max_length=10, blank=False)
	not3 = models.IntegerField(verbose_name='Nota 3', max_length=10, blank=False)
	not4 = models.IntegerField(verbose_name='Nota 4', max_length=10, blank=False)
