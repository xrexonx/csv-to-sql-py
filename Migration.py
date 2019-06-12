import MySQLdb as mdb
from utils import remove_char, parse_null_val

class Migration:
	def __init__(self, db_host, db_user, db_pass, db_name):
		# Prepare database connection
		self.conn = mdb.connect(db_host, db_user, db_pass, db_name)
		self.cursor = self.conn.cursor()

	def is_done(self, table_name):
		self.cursor.execute('select count(*) from ' + table_name + ';')
		(number_of_rows,) = self.cursor.fetchone()
		return number_of_rows > 0

	def execute(self, csv_file, csv_dir):
		table_name = csv_file.split('.')[0]
		if not self.is_done(table_name):
			print('Starting to migrate '+table_name+'....')
			print('This may take a few minutes...')
			with open(csv_dir+'/'+csv_file, 'r') as file:
				csv = file.read().splitlines()
				csv_headers = remove_char(csv[0], '"')+',LEGACY_ID'
				insert_query = 'insert into ' + table_name + ' (' +csv_headers+ ')'
				logs = []
				log_file = open('logs/'+table_name+'.txt', 'w')
				for i in range(1, len(csv)):
					legacy_id = csv[i].split(',')[0]
					csv_data = ', '.join(parse_null_val(csv[i].split(','), table_name))
					values = ' values (' + csv_data.strip() +','+legacy_id+')'
					sql = insert_query+values
					log = 'Running: '+sql+' \n'
					logs.append(log)
					print(log)
					# sql = mdb.escape_string(insert_query+values)
					self.cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
					self.cursor.execute(sql)

				log_file.writelines(logs)
				log_file.close()
				self.conn.commit()
				print('Done migrating ' + table_name)
		else:
			print(table_name+ ' data already migrated..')

	def db_close(self):
		self.cursor.execute('SET FOREIGN_KEY_CHECKS = 1;')
		print('Closing DB connection..')
		self.cursor.close()
		self.conn.close()




