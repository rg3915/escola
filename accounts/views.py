# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
# from accounts.forms import UserForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
# from .models import CreateUserTeacher, CampoMateria
from django.core.mail import send_mail
from django.db.models import Count
from .models import *
from students.models import Createstudent
from .forms import LoginForm
from django.db.models import Q
from django_easyfilters import FilterSet
''' https://django-easyfilters.readthedocs.org/en/latest/overview.html '''

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
            pessoa = authenticate(
                username=form.data['user'], password=form.data['password'])

            if pessoa is not None:
                if pessoa.is_active:
                    meu_login(request, pessoa)
                    return HttpResponseRedirect('/professor/')
                else:
                    return render(request, 'professor/prof_login.html', {'form': form})
            else:
                return render(request, 'professor/prof_login.html', {'form': form})
        else:
            return render(request, 'professor/prof_login.html', {'form': form})
    else:
        return HttpResponseRedirect('/p_login/')


def logoff(request):
    logout(request)
    return HttpResponseRedirect('/')


#===================================================================#
#                      Views for login private                      #
#===================================================================#
'''
https://django-easyfilters.readthedocs.org/en/latest/overview.html
'''


class ProfessorFilterSet(FilterSet):
    fields = [
        'id_professor',
        'materia',
        'turno',
    ]


def professor(request):
    students = CampoMateria.objects.all()
    studentsfilter = ProfessorFilterSet(students, request.GET)
    context = {'students': studentsfilter.qs, 'studentsfilter': studentsfilter}
    return render(request, 'professor/professor.html', context)

'''
@login_required()
def professor(request):
    # , 'contar': Createstudent.objects.count()})
    materia = Materia.objects.all()
    students = CampoMateria.objects.all()
    # get_serie = request.GET.get('serie_select')
    get_materia = request.GET.get('materia_select')
    get_turno = request.GET.get('turno_search_box')
    if get_materia is not None and get_turno is not None:
        students = CampoMateria.objects.filter(
            # 'materia' vem de outro model como FK, então vamos usar <select>
            Q(id_professor=request.user),
            Q(materia=get_materia),
            # 'turno' é CharField do mesmo model, então vamos usar <input>
            Q(turno__contains=get_turno)
        )
    context = {'materia': materia,
               'students': students,
               'lista': CampoMateria.objects.filter(
                   Q(id_professor=request.user))}
    return render(request, 'professor/professor.html', context)
'''
