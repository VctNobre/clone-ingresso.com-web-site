from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def filmes(request):
    return render(request, 'filmes.html')
