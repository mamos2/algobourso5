from django.db import models
from django.contrib.auth.models import User

class User_profil (models.Model):
	GENDER_CHOICES = (
		('MAL', 'Homme'),
		('FEM', 'Femme'),

	)

	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
	adress = models.CharField(max_length=200)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)


	def __str__(self):
		return self.user.username


