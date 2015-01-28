# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
#from accounts.forms import UserForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
#from .models import Pessoa, Alunos
from django.core.mail import send_mail
from django.db.models import Count
from accounts.forms import LoginForm
from students.models import Alunos
from teachers.models import Anotations



def home(request):

    return render(request, 'home.html', {'contar': Alunos.objects.count()}) #, {'contar': Alunos.objects.annotate(Count('aluno_id'))})

def p_login(request):
    form = LoginForm()
    return render(request, 'professor/prof_login.html', {'form': form})

def validar(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            pessoa = authenticate(username=form.data['login'], password=form.data['senha'])
            
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

@login_required()
def professor(request):
    return render(request,'professor/professor.html', {'lista': Anotations.objects.all(), 'contar': Alunos.objects.count()})

