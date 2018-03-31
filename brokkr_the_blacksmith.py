#!/usr/bin/python
# -*- coding: utf-8 -*-

import sbif_manager
from mimirs_well import DollarRecord

def forge(records):
	if not records:
		return

	record = records[0]

	last_record = DollarRecord.select().order_by(DollarRecord.id.desc()).get()
	last_amount = last_record.amount

	date   = record['Fecha']
	amount = float(record['Valor'].replace(',', '.'))

	DollarRecord.create(amount = amount, shift = (amount - last_amount), date = date)


class Brokkr(object):

	##########################################################
	# 	Descrición:
	# 	Método encargado de poblar la base de datos con los
	# 	valores del Dólar EE.UU. desde el año 2000.
	##########################################################
	def forge_historic_records(self):
		dollar_records = sbif_manager.get_dollar_records_since_year(1999)

		for record in dollar_records:
			date   = record['Fecha']
			amount = float(record['Valor'].replace(',', '.'))

			DollarRecord.create(amount = amount, date = date)

		dollar_records = DollarRecord.select().order_by(DollarRecord.id.asc())
		current_amount = dollar_records[0].amount

		for index in range(0, len(dollar_records)):
			shift  = dollar_records[index].amount - current_amount
			
			dollar_records[index].shift = shift
			dollar_records[index].save()

			current_amount = dollar_records[index].amount


	##########################################################
	# 	Descrición:
	# 	Método encargado de poblar la base de datos con el
	# 	valor del Dólar EE.UU. del día actual.
	##########################################################
	def forge_todays_record(self):
		dollar_records = sbif_manager.get_todays_dollar_record()
		forge(dollar_records)


	##########################################################
	# 	Descrición:
	# 	Método encargado de poblar la base de datos con el
	# 	valor del Dólar EE.UU. de un día en particular..
	##########################################################
	def forge_record_by_date(self):
		dollar_records = sbif_manager.get_dollar_record_by_date()
		forge(dollar_records)


if __name__ == '__main__':
	Brokkr().forge_historic_records()