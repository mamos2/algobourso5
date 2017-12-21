
#! /usr/bin/python3

import os, sys
import threading,time,os
def lire_contenue():
	mon_fichier = open('/home/pcapprenant15/Desktop/djma-master/data/fichier.txt', "r")
	contenu = mon_fichier.readlines(  )
	return(contenu)

