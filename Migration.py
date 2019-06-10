import MySQLdb as mdb
from emoji import emojize
from utils import remove_char

class Migration:
	def __init__(self, db_host, db_user, db_pass, db_name):
		self.conn = mdb.connect(db_host, db_user, db_pass, db_name)
		self.cursor = self.conn.cursor()

	def query(self, query):
		return self.cursor.execute(query)

	def is_done(self, table_name):
		cursor = self.conn.cursor()
		self.cursor.execute('select * from '+table_name+';')
		return cursor.fetchone()

	def nullify(self, csv_row):
		return list(map(lambda row: '0' if row == '' else row, csv_row.split(',')))

	def run_query(self, table_name):
		print(emojize(':airplane: Starting to migrate '+table_name+'....'))
		with open('data/'+table_name, 'r') as csv_file:
			csv = csv_file.read().splitlines()
			csv_headers = remove_char(csv[0], '"')
			insert_query = "insert into " + table_name + " (" +csv_headers+ ")"
			for i in range(1, len(csv)):
				csv_data = ', '.join(self.nullify(csv[i]))
				values = " values (" + csv_data + ")"
				sql = insert_query+values
				# sql = mdb.escape_string(insert_query+values)
		    	self.query('SET FOREIGN_KEY_CHECKS = 0;')
				self.query(sql)

				self.cursor.close()
				self.conn.commit()
				self.conn.close()
				print(emojize(':thumbs_up: Done migrating '+table_name))



