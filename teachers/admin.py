from django.contrib import admin
from accounts.models import CreateUserTeacher, CampoMateria, Materia, CampoProf




    	
#class MateriaDetail(admin.ModelAdmin):
	#list_display = ("teacher")



admin.site.register(CreateUserTeacher)
admin.site.register(CampoMateria)
admin.site.register(Materia)
admin.site.register(CampoProf)



