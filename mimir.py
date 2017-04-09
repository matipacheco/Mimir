import datetime
#from the_well import *

class Mimir:
	def __init__(self, matrix, year):
		self.matrix = matrix
		self.year  	= year

	def read(self):
		month = 1
		for month_amounts in self.matrix:
			day = 1
			
			for amount in month_amounts:
				try:
					date = datetime.date(self.year, month, day).isoformat()
					if amount == 0:
						DollarRecord.create(amount = None, date = date)
					else:
						DollarRecord.create(amount = amount, date = date)

				except ValueError:
					break
				
				day += 1

			month += 1

	# def set_shifts(self):
	# 	last_record = DollarRecord.select().order_by(DollarRecord.id.desc())

	# 	if last_record.exists():
	# 		last_shift  = last_record.get().shift
	# 		last_amount = last_record.get().amount
	# 	else:
	# 		last_shift  = 0.0
	# 		last_amount = 0.0