
from algobourso.models import StrategyUser
from django.db.models import DateTimeField
import threading,time,os



result = []

for x in StrategyUser.objects.filter(strategy_name="superstrategy"):
	result.append(x.date_debut) 
	result.append(x.date_fin)	


os.system('python3 ./positions.py' )