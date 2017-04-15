import numpy
import datetime

from the_well import *
from sklearn 	import linear_model

class Mimir:
  def __init__(self, model):
    self.model = model
  
  def train(self):
		records = DollarRecord.select().order_by(DollarRecord.id.asc())
		dates   = numpy.array([])
		shifts  = numpy.array([])

		for record in records:
			dates  = numpy.append(dates, int(record.date.strftime('%s')))
			shifts = numpy.append(shifts, record.shift)

		dates  = numpy.reshape(dates,  (-1, 1))
		shifts = numpy.reshape(shifts, (-1, 1))

		model = linear_model.LinearRegression(fit_intercept = True, copy_X = True)
		model.fit(dates, shifts)

		self.model = model
  
  def predict(self, date):
  	# m.predict([int(datetime.date(year, month, day).strftime('%s'))])
  	date 			 = numpy.reshape(date, (-1, 1))
  	prediction = self.model.predict(date)
  	return prediction