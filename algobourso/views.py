from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from data import positions
from data import cal
from data import nom_actions
import threading, time, os
from .models import Portefeuille 
from algobourso.models import LignePortefeuille

def index(request):
    # os.system("python/home/mams/Bureau/algobourso5-master/data/positions.py" )
    posts = cal.lire_contenue()
    #
    return render(request, 'pages/index.html', {'posts': posts})


def user(request):
    # template = loader.get_template('algobourso/index.html')

    # return HttpResponse(template.render(request))
    return render(request, 'pages/user.html')


def performance(request):
    # template = loader.get_template('algobourso/index.html')

    # return HttpResponse(template.render(request))
    return render(request, 'pages/performance.html')


def portefeuille(request):
    # template = loader.get_template('algobourso/index.html')
    profit = nom_actions.calcul_profit()
    datachat = LignePortefeuille.objects.all()
    # return HttpResponse(template.render(request))
    return render(request, 'pages/portefeuille.html', {'profit': profit} , {'datachat' : datachat})


def strategies(request):
    return render(request, 'pages/strategies.html')


def forum(request):
    return render(request, 'pages/forum.html')


def actions(request):
    return render(request, 'pages/actions.html')