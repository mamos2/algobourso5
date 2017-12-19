from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request):
    #template = loader.get_template('algobourso/index.html')

    #return HttpResponse(template.render(request))
    return render(request, 'pages/index.html')

def user(request):
    #template = loader.get_template('algobourso/index.html')

    #return HttpResponse(template.render(request))
    return render(request, 'pages/user.html')

def performance(request):
    #template = loader.get_template('algobourso/index.html')

    #return HttpResponse(template.render(request))
    return render(request, 'pages/performance.html')

def portefeuille(request):
    #template = loader.get_template('algobourso/index.html')

    #return HttpResponse(template.render(request))
    return render(request, 'pages/portefeuille.html')

def strategies(request):

    return render(request, 'pages/strategies.html')

def forum(request):

    return render(request, 'pages/forum.html')


def actions(request):
    return render(request, 'pages/actions.html')