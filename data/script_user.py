from algobourso.models import StrategyUser
from django.db.models import DateTimeField
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])



 # Argh j'ai tout écrasé !
def calcul_profit():
	mon_fichier2 = open("script.txt", "a") 
	result = []

	for x in StrategyUser.objects.filter(strategy_name="superstrategy"):
		result.append(x.date_debut) 
		result.append(x.date_fin)	



	    #self.resultat.append(donnee)
	    #self.resultat = str(self.resultat)

	mon_fichier2.write(str(result) + "\n")

	mon_fichier2.close()

