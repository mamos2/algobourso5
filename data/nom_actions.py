#! /usr/bin/python3
from algobourso.models import Portefeuille

def calcul_profit():
	result = []
	for strategy_name in Portefeuille.objects.all():
		result.append(((strategy_name.prix_vente -  strategy_name.prix_achat) * strategy_name.nbr_actions))
			
	return result
			#print(user.nbr_actions)

#calcul_profit()

