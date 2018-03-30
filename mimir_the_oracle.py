from numpy import array, append
from mimirs_well import DollarRecord

class Mimir:

	##########################################################
	# Descricion:
	# Método encargado de entrenar la Red Neuronal Recurrente.
	##########################################################
	def meditate(self):
		dollar_records = DollarRecord.select(DollarRecord.amount, DollarRecord.date).order_by(DollarRecord.id.asc())
		
		dates   = array([])
		shifts  = array([])

		for record in dollar_records:
			amounts = append(amounts, int(record.amount))
			dates   = append(dates,   int(record.date.strftime('%s')))