import os
import emoji
import MySQLdb as mdb
from dotenv import load_dotenv

class Migration:
	def __init__(self, db_host, db_user, db_pass, db_name):
		self.db_host = db_host
		self.db_user = db_user
		self.db_pass = db_pass
		self.db_name = db_name

		self.conn = db_connect()
		# load_dotenv()

	def db_connect():
		print(self.db_host)
		print(self.db_user)
		print(self.db_pass)
		print(self.db_host)
		return mdb.connect(
			self.db_host,
			self.db_user,
			self.db_pass,
			self.db_name
		)

	def is_done(table_name):
		cursor = self.conn.cursor()
		cursor.execute('select * from '+table_name+';')
		return cursor.fetchone()

    def nullify(csv_row):
        return list(map(lambda row: '0' if row == "" else row, csv_row.split(',')))

	def run_query(table_name):
		conn = self.conn
		cursor = conn.cursor()
		print(emoji.emojize(':airplane: Starting to migrate '+table_name+'....'))
		with open('data/'+table_name+'.csv', 'r') as csv_file:
	    csv = csv_file.read().splitlines()
	    csv_header = csv[0]

        for i in range(1, len(csv)):
            insert_query = "insert into " + table_name + " (" + csv_header.replace('"', '') + ")"
            csv_data = ', '.join(nullify(csv[i]))
            values = " values (" + csv_data + ")"
            sql = insert_query+values
            # sql = mdb.escape_string(insert_query+values)
            cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
            cursor.execute(sql)

        cursor.close()
		conn.commit()
		conn.close()
		print(emoji.emojize(':thumbs_up: Done migrating '+table_name))

	def execute:
		csv_files = os.listdir("data")
		if len(csv_files) > 0:
			for table_name in csv_files:
				if is_done(table_name):
					print(emoji.emojize(table_name+' already migrated :thumbs_up:'))
				else:
					# run_query(table_name)


migration = Migration('localhost', 'root', 'root', 'chuchudb')

migration.execute()