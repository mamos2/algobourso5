from django.db import models
from django.contrib.auth.models import User
import data

class User_profil (models.Model):
	GENDER_CHOICES = (
		('MAL', 'Homme'),
		('FEM', 'Femme'),

	)

	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	adress = models.CharField(max_length=200)
	gender = models.CharField(max_length=8, choices=GENDER_CHOICES)



	def __str__(self):
		return self.user.username


class StrategyUser(models.Model):
	INDICATORS_CHOICES = (
		('RSI', 'rsi'),
		('/data/indicators/macd.py', 'macd'),

	)
	date_debut = models.DateField()
	date_fin = models.DateField()
	nom = models.CharField(max_length=99)
	url_script = models.TextField()
	indicateurs_script = models.CharField(max_length=199, choices=INDICATORS_CHOICES)
	#user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
		
	
	def __str__(self):
		return self.user.username



class Portefeuille(models.Model): 
	ACTIONS_CHOICES = (
		('BNP', 'bnp'),
		('TOTAL', 'total'),

	)
		
	strategy_name = models.CharField(max_length=200)
	actions = models.CharField(max_length=49, choices=ACTIONS_CHOICES)
	date_ajout =  models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
	date_achat = models.DateField()
	date_vente = models.DateField()
	prix_achat = models.FloatField()
	prix_vente = models.FloatField()
	prix_cloture = models.FloatField()
	nbr_actions = models.IntegerField()
	benef = models.FloatField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

		
	
	def __str__(self):
		return "%s %s" % (self.strategy_name, self.user)
		
