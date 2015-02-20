# @login_required()
# def professor(request):
# , 'contar': Createstudent.objects.count()})
#     materia = Materia.objects.all()
#     students = CampoMateria.objects.all()
#     get_materia = request.GET.get('materia_select')
#     get_turno = request.GET.get('turno_search_box')
#     if get_materia is not None and get_turno is not None:
#         students = CampoMateria.objects.filter(
# 'materia' vem de outro model como FK, então vamos usar <select>
#             Q(materia=get_materia)
# 'turno' é CharField do mesmo model, então vamos usar <input>
# Q(turno__contains=get_turno)
#         )
#     context = {'materia': materia,
#                'students': students,
#                'lista': CampoMateria.objects.filter(
#                    Q(id_professor=request.user), Q(turno__contains='noite'))}
#     return render(request, 'professor/professor.html', context)


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
