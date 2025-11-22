# Start learn python code to 100 tasks https://code.mu/ru/python/tasker/stager/
# Дан словарь с датой:
from calendar import month
from unittest import result

#{
#   'year' : '2025',
#	'month': '12',
#	'day'  : '31',
#}
#Из элементов этого словаря соберите дату в следующем формате:

#'2025-12-31'

dict={

	'year' : '2025',
	'month': '12',
	'day'  : '31',
}
print(dict['year']+"-"+dict['month']+"-"+dict['day']) # через запятую с пробелами, через + слитно

