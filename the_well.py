import settings

from peewee  import *
from MySQLdb import *

# CREATE TABLE dollar_records (
#     id INT NOT NULL AUTO_INCREMENT,
#     amount FLOAT,
#     shift  FLOAT,
#     date   DATE,
#    	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#    	PRIMARY KEY (id)
# );

# ALTER TABLE dollar_records ADD interpolated_amount FLOAT AFTER amount;

# CREATE TABLE copper_records (
#     id INT NOT NULL AUTO_INCREMENT,
#     amount FLOAT,
#     date   DATE,
#    	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#    	PRIMARY KEY (id)
# );

db = MySQLDatabase( settings.DATABASE_NAME,
										user 		= settings.DATABASE_USER,
										passwd 	= settings.DATABASE_PASS,
										host 		= settings.DATABASE_HOST
									)

class DollarRecord(Model):
	id                  = IntegerField()
	amount              = FloatField()
	interpolated_amount = FloatField()
	shift               = FloatField()
	date                = DateField()
	class Meta:
		database = db
		db_table = 'dollar_records'

class CopperRecord(Model):
	id                  = IntegerField()
	amount              = FloatField()
	interpolated_amount = FloatField()
	shift               = FloatField()
	date                = DateField()
	class Meta:
		database = db
		db_table = 'copper_records'
