# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
#from accounts.forms import UserForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
#from .models import CreateUserTeacher, CampoMateria
from django.core.mail import send_mail
from django.db.models import Count
from .models import *
from students.models import Createstudent
from .forms import LoginForm
from django.db.models import Q


#===================================================================#
#                         Views Index                               #
#===================================================================#
def home(request):
    return render(request, 'home.html')


#===================================================================#
#                         Views autentication                       #
#===================================================================#
def p_login(request):
    form = LoginForm()
    return render(request, 'professor/prof_login.html', {'form': form})

def validar(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            pessoa = authenticate(username=form.data['user'], password=form.data['password'])
            
            if pessoa is not None:
                if pessoa.is_active:
                    meu_login(request, pessoa)
                    return HttpResponseRedirect('/professor/')
                else:
                    return render(request, 'professor/prof_login.html', {'form': form})
            else:
                return render(request, 'professor/prof_login.html', {'form': form})
        else:
            return render(request,'professor/prof_login.html',{'form':form})
    else:
        return HttpResponseRedirect('/p_login/')

def logoff(request):
    logout(request)
    return HttpResponseRedirect('/')


#===================================================================#
#                      Views for login private                      #
#===================================================================#
@login_required()
def professor(request):
    return render(request,'professor/professor.html',
     {'lista': CampoMateria.objects.filter(id_professor=request.user)}) 
     #, 'contar': Createstudent.objects.count()})


def get_queryset(self):
    students = CampoMateria.objects.all()
    get_serie = self.request.GET.get('serie_box')
    get_turno = self.request.GET.get('turno_box')
    get_materia = self.request.GET.get('materia_box')
    students = students.filter(
        Q(turma__contains=get_serie),
        Q(turno_contains=get_turno),
        Q(materia_contains=get_materia)
    )
    return students