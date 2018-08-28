#!/usr/bin/python
# -*- coding: utf-8 -*-

from mimirs_well import DollarRecord

from datetime import date

from numpy import array, append, reshape
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense, LSTM, Dropout


class Mimir:

	##########################################################
	# Descripción:
	# Inicializador de la clase.
	##########################################################
	def __init__(self):
		self.regressor = None


	##########################################################
	# Descripción:
	# Método encargado de entrenar la Red Neuronal Recurrente.
	##########################################################
	def meditate(self):
		shifts       = array([])
		train_shifts = DollarRecord.select(DollarRecord.shift).where(DollarRecord.date < date.today().replace(day = 1)).order_by(DollarRecord.id.asc()).tuples()

		for shift in train_shifts:
			shifts = append(shifts, shift)

		shifts = shifts.reshape(-1, 1)

		scaler        = MinMaxScaler(feature_range = (0, 1))
		scaled_shifts = scaler.fit_transform(shifts)

		x_train, y_train = [], []

		for i in range(60,len(shifts)):
			# y tiene el valor del dólar el 60-ésimo día, mientras que x tiene el valor del dólar de los 59 días anteriores.
			x_train.append(scaled_shifts[(i - 60):i, 0])
			y_train.append(scaled_shifts[i         , 0])

		x_train, y_train = array(x_train), array(y_train)

		x_train = reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
		
		regressor = Sequential()
		regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (x_train.shape[1], 1)))
		regressor.add(Dropout(rate = 0.2))

		regressor.add(LSTM(units = 50, return_sequences = True))
		regressor.add(Dropout(rate = 0.2))

		regressor.add(LSTM(units = 50, return_sequences = True))
		regressor.add(Dropout(rate = 0.2))

		regressor.add(LSTM(units = 50, return_sequences = False))
		regressor.add(Dropout(rate = 0.2))

		regressor.add(Dense(units = 1))

		regressor.compile(optimizer = 'rmsprop', loss = 'mean_squared_error') # probar con optimizer = 'rmsprop'
		regressor.fit(x_train, y_train, epochs = 50, batch_size = 32)

		self.regressor = regressor
		self.store_model()


	##########################################################
	# Descripción:
	# Método encargado de probar el modelo.
	##########################################################
	# def test(self):
	# 	shifts_array       = array([])
	# 	total_shifts_array = array([])

	# 	total_shifts = DollarRecord.select(DollarRecord.shift).order_by(DollarRecord.id.asc()).tuples()
	# 	test_shifts  = total_shifts.where(DollarRecord.date >= date.today().replace(day = 1))

	# 	for shift in test_shifts:
	# 		shifts_array = append(shifts_array, shift)

	# 	for shift in total_shifts_array:
	# 		total_shifts_array = append(total_shifts_array, shift)

	# 	shifts_array       = shifts_array.reshape(-1, 1)
	# 	total_shifts_array = total_shifts_array.reshape(-1, 1)


	##########################################################
	# Descripción:
	# Método encargado de guardar el modelo.
	##########################################################
	def store_model(self):
		model      = self.regressor
		model_json = model.to_json()

		with open("model/model.json", "w") as model_file:
			model_file.write(model_json)

		model.save_weights("model/model.h5")


	##########################################################
	# Descripción:
	# Método encargado de realizar las predicciones del modelo.
	##########################################################
	def predict(self):
		model_file = open("model/model.json", "r")
		model_json = model_file.read()

		model_file.close()

		model = model_from_json(model_json)
		model.load_weights("model.h5")

		return


if __name__ == '__main__':
	mimir = Mimir()
	mimir.meditate()
	mimir.test()