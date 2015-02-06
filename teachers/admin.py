from django.contrib import admin
from accounts.models import CreateUserTeacher, Materia




    	
#class MateriaDetail(admin.ModelAdmin):
	#list_display = ("teacher")



admin.site.register(CreateUserTeacher)
admin.site.register(Materia)



