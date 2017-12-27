#! /usr/bin/python3
from algobourso.models import Portefeuille
from algobourso.models import LignePortefeuille

"""def calcul_profit():
	result = []
	for strategy_name in LignePortefeuille.objects.all():
		result.append(((strategy_name.prix_vente -  strategy_name.prix_achat) * strategy_name.nbr_actions))
			
	return result"""
			#print(user.nbr_actions)

#calcul_profit()

def calcul_profit():
	result = []
	for portefeuille in LignePortefeuille.objects.all():
		result.append(portefeuille.actions + "  " + str(portefeuille.prix_achat) )
			
	return result

