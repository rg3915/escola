from django import forms
#from .models import Pessoa


"""
class PessoaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Pessoa
"""
class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)

