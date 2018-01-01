from algobourso.models import StrategyUser
from django.db.models import DateTimeField
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])



def calcul_profit():
	result = []

	for x in StrategyUser.objects.filter(strategy_name="superstrategy"):
		result.append(str(x.date_debut))
		result.append(str(x.date_fin))	
		toto = result[0]
		titi = result[1]
		mon_fichier = open("script_user.txt", "a")
		donnee = ("-fromdate"+ " " + toto + " " + titi )
		print (donnee)

