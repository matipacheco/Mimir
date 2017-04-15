import datetime

from the_well import *
from sklearn 	import linear_model

class Mimir:
	def __init__(self, matrix, year):
		self.matrix = matrix
		self.year  	= year

	def read(self):
		last_record 			= DollarRecord.select().order_by(DollarRecord.id.desc()).get()
		last_record_date 	= last_record.date
		month 						= 1

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

	# def set_shifts(self):
	# 	last_record = DollarRecord.select(date).order_by(DollarRecord.id.desc())

	# 	if last_record.exists():
	# 		last_shift  = last_record.get().shift
	# 		last_amount = last_record.get().amount
	# 	else:
	# 		last_shift  = 0.0
	# 		last_amount = 0.0

	# def think(self):
	# 	log_reg = linear_model.LogisticRegression()