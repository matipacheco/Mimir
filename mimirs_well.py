import settings
import datetime
from peewee  import *
from MySQLdb import *

db = MySQLDatabase(	settings.DATABASE_NAME,
					user   = settings.DATABASE_USER,
					passwd = settings.DATABASE_PASS,
					host   = settings.DATABASE_HOST
				)

class DollarRecord(Model):
	id         = PrimaryKeyField()
	amount     = FloatField()
	shift      = FloatField(default = 0.0)
	date       = DateField()
	created_at = DateTimeField(default = datetime.datetime.now)
	updated_at = DateTimeField(default = datetime.datetime.now)
	class Meta:
		database = db
		db_table = 'dollar_records'


if __name__ == '__main__':
	db.connect()
	db.create_tables([DollarRecord])