from django.contrib import admin
from .models import Createteacher, Materias, Alunos, Anotations



class MemberDetailAdmin(admin.ModelAdmin):
    list_display = ("teacher", "registry_mec", "graduation", "address", "cep")
    	
class MateriaDetail(admin.ModelAdmin):
	list_display = ("prof", "materia1", "materia2", "materia3")


admin.site.register(Createteacher, MemberDetailAdmin)
admin.site.register(Materias, MateriaDetail)
admin.site.register(Alunos)
admin.site.register(Anotations)

