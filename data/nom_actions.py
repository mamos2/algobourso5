#! /usr/bin/python3
"""from algobourso.models import Portefeuille
from algobourso.models import LignePortefeuille"""
from algobourso.models import StrategyUser
from django.db.models import DateTimeField
import datetime  # For datetime objects
import os.path  # To manage paths
import sys 
"""def calcul_profit():
	result = []
	for strategy_name in LignePortefeuille.objects.all():
		result.append(((strategy_name.prix_vente -  strategy_name.prix_achat) * strategy_name.nbr_actions))
			
	return result"""
			#print(user.nbr_actions)

#calcul_profit()

"""def calcul_profit():
	result = []
	for portefeuille in LignePortefeuille.objects.all():
		result.append(portefeuille.actions + "  " + str(portefeuille.prix_achat) )
			
	return result"""

def calcul_profit():
	result = []

	for x in StrategyUser.objects.filter(strategy_name="superstrategy"):
		result.append(str(x.date_debut))
		result.append(str(x.date_fin))
		result.append(str(x.setcash))
		result.append(str(x.actions))
		result.append(str(x.sma.params))
		datefirst = result[0]
		datelast = result[1]
		setcash = result[2]
		actions = result[3]
		sma = result[4]

	
		
		donnee = ("-fromdate "+ datefirst + " " + "-todate"+ " " +datelast + " " + "-setcash " +setcash + " "+ actions
			+" " + "--smaperiod " +sma)
		return (donnee)

""">>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()"""