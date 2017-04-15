import numpy
import datetime

from the_well import *
from sklearn 	import linear_model

class Mimir:
  def __init__(self, model):
    self.model = model
  
  def train(self):
		records = DollarRecord.select().where(DollarRecord.amount != None)
		dates   = numpy.array([])
		amounts = numpy.array([])

		for record in records:
			dates   = numpy.append(dates, int(record.date.strftime('%s')))
			amounts = numpy.append(amounts, record.amount)
			
			dates   = numpy.reshape(dates, (-1, 1))
			amounts = numpy.reshape(amounts, (-1, 1))

			model = linear_model.LinearRegression(fit_intercept = True, copy_X = True)
			model.fit(dates, amounts)

		self.model = model
  
  def predict(self, date):
  	date 			 = numpy.reshape(date, (-1, 1))
  	prediction = self.model.predict(date)
  	return prediction