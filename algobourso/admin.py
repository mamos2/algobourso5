from django.contrib import admin
from .models import User_profil
from .models import StrategyUser
from .models import Portefeuille
from .models import LignePortefeuille
from .models import sma
#from .models import ActionData

#admin.site.register(ActionData)
admin.site.register(User_profil)
admin.site.register(StrategyUser)
admin.site.register(Portefeuille)
admin.site.register(LignePortefeuille)
admin.site.register(sma)