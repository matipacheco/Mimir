#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

from settings import SBIF_API_KEY

##########################################################
#	Descripción:
#	Permite obtener un listado en xml o json con el valor
#	del Dólar EE.UU. para los años siguientes al año que
#	se indique.
##########################################################
def get_dollar_records_since_year(year):
	url      = 'http://api.sbif.cl/api-sbifv3/recursos_api/dolar/posteriores/' + str(year) + '?apikey=' + SBIF_API_KEY + '&formato=json'
	response = requests.get(url).json()

	try:
		return response['Dolares']
	except KeyError as e:
		return []


##########################################################
#	Descripción:
#	Permite obtener un listado con el valor del Dólar.
#	EE.UU. para el día actual.
##########################################################
def get_todays_dollar_record():
	url      = 'http://api.sbif.cl/api-sbifv3/recursos_api/dolar?apikey=' + SBIF_API_KEY + '&formato=json'
	response = requests.get(url).json()

	try:
		return response['Dolares']
	except KeyError as e:
		return []


##########################################################
#	Descripción:
#	Permite obtener un listado con el valor del Dólar.
#	EE.UU. para un día en particular
##########################################################
def get_dollar_record_by_date():
	date = input('Ingrese fecha (en formato dd/mm/yyyy): ')
	date = date.split('/')

	url      = 'http://api.sbif.cl/api-sbifv3/recursos_api/dolar/' + date[2] + '/' + date[1] + '/dias/' + date[0] + '?apikey=' + SBIF_API_KEY + '&formato=json'
	response = requests.get(url).json()

	try:
		return response['Dolares']
	except KeyError as e:
		return []
	