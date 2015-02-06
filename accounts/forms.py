from django import forms
from .models import UserModel



"""
class PessoaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Pessoa
"""
#===================================================================#
#                         Form Login                                #
#===================================================================#
class LoginForm(forms.ModelForm):
	password = forms.CharField(max_length=30)

	class Meta:
		model = UserModel
		widgets = {
        	'password': forms.PasswordInput(),
    	}

