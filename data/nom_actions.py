#! /usr/bin/python3
from algobourso.models import Portefeuille

def calcul_profit():

	for user in Portefeuille.objects.all():
		return((user.prix_vente -  user.prix_achat) * user.nbr_actions)
		#print(user.nbr_actions)

#calcul_profit()

