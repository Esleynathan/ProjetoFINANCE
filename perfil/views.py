from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conta

def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    return render(request, 'gerenciar.html')

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        return redirect('/perfil/gerenciar/')
    
    conta = Conta(
        apelido = apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()

    return redirect('/perfil/gerenciar/')