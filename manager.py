import numpy
import datetime

from the_well import *

class Manager:
	def __init__(self, matrix, year):
		self.matrix = matrix
		self.year  	= year

##########################################################
# Descricion:
# Inserta una entrada en la tabla dollar_records.
##########################################################
	def insert_copper_record(self, parsed_amount):
		CopperRecord.create(amount = parsed_amount, date = datetime.date.today().isoformat())


##########################################################
# Descricion:
# Inserta una entrada en la tabla dollar_records.
##########################################################
	def insert_dollar_record(self):
		last_record      = DollarRecord.select().order_by(DollarRecord.id.desc()).get()
		last_record_date = last_record.date
		month            = 1

		for month_amounts in self.matrix:
			day = 1
			
			for amount in month_amounts:
				try:
					date = datetime.date(self.year, month, day)

					if last_record_date < date < datetime.date.today():
						if amount == 0:
							DollarRecord.create(amount = None, date = date.isoformat())
						
						else:
							DollarRecord.create(amount = amount, date = date.isoformat())

					elif date > datetime.date.today():
						break

					else:
						continue

				except ValueError:
					break

				finally:
					day += 1

			month += 1


##########################################################
# Descricion:
# Setea los interpolated_amounts y shifts. Estaba pensado
# para ser ejecutado una unica vez, pues despues de este
# punto se empieza a predecir los valores.
##########################################################
	def copper_records_setup(self):
		records = DollarRecord.select().order_by(DollarRecord.id.asc())
		amounts = numpy.array([])

		for record in records:
			if record.amount == None:
				amounts = numpy.append(amounts, numpy.NaN)
			
			else:
				amounts = numpy.append(amounts, record.amount)
		
		nans          = numpy.isnan(amounts)
		amounts[nans] = numpy.interp(numpy.flatnonzero(nans), numpy.flatnonzero(~nans), amounts[~nans])

		amount = amounts[0]

		for index in range(0, len(amounts)):
			shift  = amounts[index] - amount
			
			records[index].shift               = shift
			records[index].interpolated_amount = amounts[index]
			records[index].save()

			amount = amounts[index]


##########################################################
# Descricion:
# Lee las planillas excel con los valores de libra de
# cobre y los inserta en la tabla copper_records.
##########################################################
#	def copper_records_setup(self):