import os
import MySQLdb as mdb
from emoji import emojize
from utils import remove_char

class Migration:
	def __init__(self, db_host, db_user, db_pass, db_name):
		self.conn = mdb.connect(db_host, db_user, db_pass, db_name)
		self.cursor = self.conn.cursor()

	def query(self, query, params):
		return self.cursor.execute(query)

	def is_done(table_name):
		cursor = self.conn.cursor()
		self.cursor.execute('select * from '+table_name+';')
		return cursor.fetchone()

	def nullify(csv_row):
		return list(map(lambda row: '0' if row == '' else row, csv_row.split(',')))

	def run_query(table_name):
		conn = self.conn
		cursor = self.cursor
		print(emojize(':airplane: Starting to migrate '+table_name+'....'))
		with open('data/'+table_name, 'r') as csv_file:
		    csv = csv_file.read().splitlines()
		    csv_header = remove_char(csv[0], '"')
		    for i in range(1, len(csv)):
		    	insert_query = "insert into " + table_name + " (" +csv_header+ ")"
		    	print(insert_query)
		    	csv_data = ', '.join(nullify(csv[i]))
		    	values = " values (" + csv_data + ")"
		    	sql = insert_query+values
		    	 # sql = mdb.escape_string(insert_query+values)
		    	query('SET FOREIGN_KEY_CHECKS = 0;')
		    	query(sql)
		cursor.close()
		conn.commit()
		# conn.close()
		print(emojize(':thumbs_up: Done migrating '+table_name))

	def __del__(self):
		self.conn.close()


