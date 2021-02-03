from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import FormularioLogin, FormularioRegistroUsuario
from django.contrib.auth.decorators import login_required
from .models import Mixin

'''
def login_usuario(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            cd = formulario.cleaned_data
            user = authenticate(request, 
                                username = cd['nome_usuario'],
                                password = cd['senha'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autenticado' 'Sucesso')
                else:
                    return HttpResponse('Conta está desativada')
            else:
                return HttpResponse('Login Inválido')
    else:
        formulario = FormularioLogin()
        
    return render(request, 'conta/login.html', {'formulario':formulario})
'''

@login_required
def painel_controle(request):
    usuario = Mixin.objects.all()
    return render(request, 'conta/painel_controle.html', {'section':'painel de controle', 'usuario':usuario})

def registrar(request):
    if request.method == 'POST':
        formulario_usuario = FormularioRegistroUsuario(request.POST)
        if formulario_usuario.is_valid():
            novo_usuario = formulario_usuario.save(commit=False)
            novo_usuario.set_password(formulario_usuario.cleaned_data['senha'])
            novo_usuario.save()
            return render(request, 'conta/registro_realizado.html', {'formulario_usuario':formulario_usuario})
    else:
        formulario_usuario = FormularioRegistroUsuario()
    return render(request, 'conta/registrar.html', {'formulario_usuario':formulario_usuario})