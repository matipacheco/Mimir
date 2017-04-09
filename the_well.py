from peewee import *
import settings
import MySQLdb

# CREATE TABLE dollar_records (
#     id INT NOT NULL AUTO_INCREMENT,
#     amount DECIMAL(10),
#     shift  DECIMAL(10),
#     date   DATETIME,
#    	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#    	PRIMARY KEY (id)
# );

db = MySQLDatabase( settings.DATABASE_NAME,
										user 		= settings.DATABASE_USER,
										passwd 	= settings.DATABASE_PASS,
										host 		= settings.DATABASE_HOST
									)
		
class DollarRecord(Model):
	id      = IntegerField()
	amount  = FloatField()
	shift		= FloatField()
	date 		= DateField()
	class Meta:
		database = db
		db_table = 'dollar_records'