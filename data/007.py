#!/usr/bin/python3

import threading,time,os


actions= {"AAPL" : "apple.cvs" , "^FCHI": "cac40.csv" , "ORA.PA": "orange.csv" , "FP.PA":"total.csv" , "BTCEUR=X" : "bitcoin.csv",}

for code, nom_fichier in actions.items():
	os.system("python3 /home/pcapprenant15/Desktop/certif222/backtrader-master/tools/yahoodownload.py --ticker" + " " + code  + " " + "--fromdate 2015-07-07 --todate 2017-11-11 --outfile" + " " + nom_fichier)
	
