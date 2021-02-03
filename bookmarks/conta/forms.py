from django import forms
from .models import Mixin
from django.contrib.auth.models import User

class FormularioLogin(forms.Form):
    nome_usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)


class FormularioRegistroUsuario(forms.ModelForm):
    senha = forms.CharField(label='senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Repetir senha', widget=forms.PasswordInput)

    class Meta:
        model = Mixin
        fields = ('username', 'first_name', 'email', 'doce_preferido')
    
    def  limpar_senha2(self):
        cd = self.cleaned_data
        if cd['senha'] != cd['senha2']:
            raise forms.ValidationError('As senhas não são iguais')
        return cd['senha2']