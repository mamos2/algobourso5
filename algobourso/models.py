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
	
	date_debut = models.DateField()
	date_fin = models.DateField()
	stratname = models.CharField(max_length=99)
	setcash = models.IntegerField()
	#user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	
	
	def __str__(self):
		return self.stratname

class Indicateurs(models.Model):
	
	signal_dachat = models.BooleanField()
	signal_vente = models.BooleanField()
	signal_vad = models.BooleanField()
	signal_rachat = models.BooleanField()

	strategyuser = models.ManyToManyField(StrategyUser)	
	
	def __int__(self):
		return self.indicateurs.strategyuser.stratname

class sma(models.Model):
	params = models.IntegerField()
	close_over_sma = models.NullBooleanField( )
	close_less_sma = models.NullBooleanField( )
	indicateurs = models.ForeignKey(Indicateurs, blank=True, null=True, on_delete=models.CASCADE)
	#user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	#strategyUser = models.ManyToManyField(StrategyUser)	

	def __int__(self):
		return self.indicateurs.strategyuser.stratname

class Portefeuille(models.Model): 
	portefeuille_name = models.CharField(max_length=200)	
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return (self.portefeuille_name )


class LignePortefeuille(models.Model): 
	ACTIONS_CHOICES = (
		('BNP', 'bnp'),
		('TOTAL', 'total'),

	)
	
	portefeuille = models.ForeignKey(Portefeuille, on_delete=models.CASCADE)
	actions = models.CharField(max_length=49, choices=ACTIONS_CHOICES)
	date_ajout =  models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
	date_achat = models.DateField()
	date_vente = models.DateField()
	prix_achat = models.FloatField()
	prix_vente = models.FloatField()
	prix_cloture = models.FloatField()
	nbr_actions = models.IntegerField()
	#benef = models.FloatField()
	
		
	
	def __str__(self):
		return (self.actions)
		

