import numpy
import datetime

from the_well import *

class Manager:
	def __init__(self, matrix, year):
		self.matrix = matrix
		self.year  	= year

	def insert(self):
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

					else:
						return

				except ValueError:
					break
				
				day += 1

			month += 1

	def initial_setup(self):
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
		