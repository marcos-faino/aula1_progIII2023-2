
from django.shortcuts import render, HttpResponse
from django.views import View
from django.template import loader


def index(request):
    return HttpResponse(f"<h1>Minha Primeira Página Django</h1>"                        
                        f"<h3>Olá, seja bem vindo")

def indexcomnome(request, nome):
    return HttpResponse(f"<h1>Minha Primeira Página Django</h1>"

                        f"<h3>Olá,{nome}, seja bem vindo")


def soma(request, num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    soma = n1+n2
    return HttpResponse(f'<p>A soma de {num1} + {num2} é {soma}')


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, nome):
        conteudo = loader.render_to_string(self.template_name, context={'nome': nome})
        return HttpResponse(conteudo)