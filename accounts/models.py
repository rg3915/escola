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
#                         Create user teacher                       #
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
	id_professor = models.ForeignKey(User)
	aluno = models.ForeignKey(Createstudent)
	turno = models.CharField(verbose_name=u'Turno',  max_length=20)
	serie = models.CharField(verbose_name=u'Serie', max_length=30)
	materia = models.CharField(verbose_name='Materia', max_length=20, choices= MATERIA_CHOICES)

	def __unicode__(self):
		return unicode(self.aluno)

