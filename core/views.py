from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request,idade, nome=''):
    return HttpResponse(f"<h1>Minha Primeira Página Django</h1>"
                        
                        f"<h3>Olá {nome}, {idade} anos, seja bem vindo")
