from django.shortcuts import render
import requests
import json

def index(request):
    filmes_cartaz = requests.get('https://ingressoapi.herokuapp.com/filmes/cartaz/') 
    filmes_alta = requests.get('https://ingressoapi.herokuapp.com/filmes/alta/') 
    dados = {
        'filmes_cartaz': json.loads(filmes_cartaz.content),
        'filmes_alta': json.loads(filmes_alta.content),
    }
    return render(request, 'index.html', dados)

def filmes(request):
    todos_filmes = requests.get('https://ingressoapi.herokuapp.com/filmes/')
    dados = {
        'filmes': json.loads(todos_filmes.content)
    }
    return render(request, 'filmes.html', dados)
