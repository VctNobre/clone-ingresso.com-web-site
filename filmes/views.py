from django.shortcuts import render
import requests
import json

def index(request):
    requisisao = requests.get('https://ingressoapi.herokuapp.com/filmes/')
    dados = {
        'filmes': json.loads(requisisao.content)
    }
    return render(request, 'index.html', dados)

def filmes(request):
    return render(request, 'filmes.html')
