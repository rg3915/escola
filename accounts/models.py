# coding: utf-8
from django.contrib.auth.models import User
from django.db import models
from students.models import Createstudent
from .materias import *


#===================================================================#
#                         Model Login                               #
#===================================================================#
class UserModel(models.Model):
	user = models.CharField(verbose_name='User', max_length=200)
	

	def __unicode__(self):
		return self.use

#===================================================================#
#                         Create teacher                            #
#===================================================================#
class CreateUserTeacher(models.Model):
	id_teacher = models.AutoField(primary_key=True)
	teacher = models.CharField(verbose_name='Professor', max_length=100)

	class Meta:
		verbose_name='Cadastro de professor'
		verbose_name_plural='Cadastro de professores'

	def __unicode__(self):
		return self.teacher

#===================================================================#
#                  Model Materia Private for users                  #
#===================================================================#
class Materia(models.Model):
	materia = models.CharField(verbose_name='Materia', max_length=40)

	class Meta:
		verbose_name='Materia'
		verbose_name_plural='Materias'
	

	def __unicode__(self):
		return self.materia


class CampoMateria(models.Model):
	id_professor = models.ForeignKey(User)
	aluno = models.ForeignKey(Createstudent)
	turno = models.CharField(verbose_name=u'Turno',  max_length=20)
	serie = models.CharField(verbose_name=u'Serie', max_length=30)
	nota = models.DecimalField(verbose_name='Nota', max_digits=10, decimal_places=2)
	falta = models.IntegerField(verbose_name='Falta', blank=True, null=True)
	materia = models.ForeignKey(Materia, verbose_name='Materia')

	class Meta:
		verbose_name='Campo Materia'
		verbose_name_plural='Campos das Materias'
	

	def __unicode__(self):
		return unicode(self.aluno)

class CampoProf(models.Model):
	id_professor = models.ForeignKey(User)
	Campo_materia = models.ForeignKey(CampoMateria)

	class Meta:
		verbose_name='Campo Professor'
		verbose_name_plural='Campos dos Professores'
	

	def __unicode__(self):
		return unicode(self.id_professor)

	"""
	materia_1 = models.CharField(verbose_name='Materia 1', max_length=20, choices= MATERIA_CHOICES)
	materia_2 = models.CharField(verbose_name='Materia 2', max_length=20, choices= MATERIA_CHOICES, blank=True)
	materia_3 = models.CharField(verbose_name='Materia 3', max_length=20, choices= MATERIA_CHOICES, blank=True)
	materia_4 = models.CharField(verbose_name='Materia 4', max_length=20, choices= MATERIA_CHOICES, blank=True)
	materia_5 = models.CharField(verbose_name='Materia 5', max_length=20, choices= MATERIA_CHOICES, blank=True)
	"""