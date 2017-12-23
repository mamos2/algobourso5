from django.contrib import admin
from .models import User_profil
from .models import StrategyUser
from .models import Portefeuille

admin.site.register(User_profil)
admin.site.register(StrategyUser)
admin.site.register(Portefeuille)