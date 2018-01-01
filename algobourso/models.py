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

"""class ActionData(models.Model):
	ACTIONS_CHOICES = (
		('/data/apple.csv', 'apple'),
		('TOTAL', 'total'),

	)
	

	actions = models.CharField(max_length=49, choices=ACTIONS_CHOICES)
	
	

	def __str__(self):
		return (self.actions)"""

class sma(models.Model):

	params = models.IntegerField()
	close_over_sma = models.NullBooleanField( default=0)
	close_less_sma = models.NullBooleanField( default=0)
	#user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	#strategyUser = models.ManyToManyField(StrategyUser)	
	def __int__(self):
		return self.params

class StrategyUser(models.Model):
	ACTIONS_CHOICES = (
		('/data/apple.csv', 'apple'),
		('TOTAL', 'total'),

	)
	
	date_debut = models.DateField()
	date_fin = models.DateField()
	strategy_name = models.CharField(max_length=99)

	

	actions = models.CharField(max_length=49, blank=True, null=True, choices=ACTIONS_CHOICES)
	signal_dachat = models.BooleanField(default=1)
	signal_vente = models.BooleanField(default=0)
	signal_vad = models.BooleanField(default=0)
	signal_rachat = models.BooleanField(default=0)
	setcash = models.IntegerField()
	#user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	#actions = models.ManyToManyField(ActionData)
	sma = models.ForeignKey(sma, blank=True, null=True, on_delete=models.CASCADE)


	
	
	def __str__(self):
		return self.strategy_name






class Portefeuille(models.Model): 
	portefeuille_name = models.CharField(max_length=200)	
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return (self.portefeuille_name )


class LignePortefeuille(models.Model): 
	
	
	portefeuille = models.ForeignKey(Portefeuille, on_delete=models.CASCADE)
	date_ajout =  models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
	date_achat = models.DateField()
	date_vente = models.DateField()
	prix_achat = models.FloatField()
	prix_vente = models.FloatField()
	prix_cloture = models.FloatField()
	nbr_actions = models.IntegerField()
	#benef = models.FloatField()
	
		
	
	def __str__(self):
		return (self.nbr_actions)
		

