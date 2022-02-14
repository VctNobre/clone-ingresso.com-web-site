from django.shortcuts import render
import requests
import json

def index(request):
   
    filmes_cartaz = requests.get('https://ingressoapi.herokuapp.com/filmes/cartaz/') 
    filmes_alta = requests.get('https://ingressoapi.herokuapp.com/filmes/alta/') 
    noticias = requests.get('https://ingressoapi.herokuapp.com/noticias/')
    banner = requests.get('https://ingressoapi.herokuapp.com/filmes/principal/') 
    fan_shop = requests.get('https://ingressoapi.herokuapp.com/fanshop/')
    filmes_em_breve = requests.get('https://ingressoapi.herokuapp.com/filmes/breve/')
    dados = {
        'filmes_cartaz': json.loads(filmes_cartaz.content),
        'filmes_alta': json.loads(filmes_alta.content),
        'noticias':json.loads(noticias.content),
         'banner': json.loads(banner.content)[0],
         'fan_shop': json.loads(fan_shop.content),
         'filmes_breve': json.loads(filmes_em_breve.content)[0:10],
    }
    return render(request, 'index.html', dados)

def filmes(request):
    todos_filmes = requests.get('https://ingressoapi.herokuapp.com/filmes/')
    filmes_em_breve = requests.get('https://ingressoapi.herokuapp.com/filmes/breve/')
    dados = {
        'filmes': json.loads(todos_filmes.content),
        'filmes_breve': json.loads(filmes_em_breve.content),
    }
    return render(request, 'filmes.html', dados)


def cinemas(request):
    return render(request, 'cinemas.html')
