import numpy
import datetime

from the_well import *
from sklearn 	import linear_model

class Mimir:
  def __init__(self, dates):
    self.dates = dates
  
  def predict(self):
		records = DollarRecord.select().order_by(DollarRecord.id.asc())
		dates   = numpy.array([])
		shifts  = numpy.array([])

		for record in records:
			dates  = numpy.append(dates,  int(record.date.strftime('%s')))
			shifts = numpy.append(shifts, int(record.shift))

		dates  = numpy.reshape(dates,  (-1, 1))
		shifts = numpy.reshape(shifts, (-1, 1))

		model = linear_model.LogisticRegression()
		model.fit(dates, shifts.ravel())

		dates      = numpy.reshape(self.dates, (-1, 1))
		prediction = model.predict(dates)
		return prediction

	#def notify(self):
		#pass