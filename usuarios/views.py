from  django.shortcuts import render
from .forms import Cadastro

def cadastro (request):
    form = Cadastro()
    contexto = {
        'form':form
    }
    return render(request, 'cadastro.html', contexto)
