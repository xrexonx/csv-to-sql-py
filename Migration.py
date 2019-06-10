import MySQLdb as mdb
from utils import remove_char, parse_csv_null_val

class Migration:
	def __init__(self, db_host, db_user, db_pass, db_name):
		self.conn = self.db_prepare(db_host, db_user, db_pass, db_name)
		self.cursor = self.conn.cursor()

	def db_prepare(self, db_host, db_user, db_pass, db_name):
		return mdb.connect(db_host, db_user, db_pass, db_name)

	def query_exec(self, query):
		return self.cursor.execute(query)

	def is_done(self, table_name):
		self.cursor.execute('select count(*) from ' + table_name + ';')
		(number_of_rows,) = self.cursor.fetchone()
		return number_of_rows > 0

	def run_query(self, csv_file, csv_dir):
		table_name = csv_file.split('.')[0]
		if not self.is_done(table_name):
			print('Starting to migrate '+table_name+'....')
			print('This may take a few minutes...')
			with open(csv_dir+'/'+csv_file, 'r') as file:
				csv = file.read().splitlines()
				csv_headers = remove_char(csv[0], '"')
				insert_query = "insert into " + table_name + " (" +csv_headers+ ")"
				for i in range(1, len(csv)):
					csv_data = ', '.join(parse_csv_null_val(csv[i].split(','), '0'))
					values = " values (" + csv_data.strip() + ")"
					sql = insert_query+values
					# sql = mdb.escape_string(insert_query+values)
					# Disable foreignkey checking for insertion
					self.query_exec('SET FOREIGN_KEY_CHECKS = 0;')
					self.query_exec(sql)

				self.conn.commit()
				print('Done migrating ' + table_name)
		else:
			print(table_name+ ' data already migrated..')

	def db_close(self):
		self.query_exec('SET FOREIGN_KEY_CHECKS = 1;')
		print('Closing DB connection..')
		self.cursor.close()
		self.conn.close()




