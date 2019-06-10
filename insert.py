import os
import emoji
import MySQLdb as mdb
from dotenv import load_dotenv

# Load environment
load_dotenv()

ENV = os.getenv("ENV")
DATA_DIR = os.getenv("DATA_DIR")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

conn = mdb.connect(db_host, db_user, db_pass, db_name)
cursor = conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS `mm_db`;')
cursor.execute('USE `mm_db`;')

# should be dynamic
table_name = 'STATE'

with open(DATA_DIR+'/'+ENV+'/'+table_name+'.csv', 'r') as csv_file:
    csv = csv_file.read().splitlines()
    csv_header = csv[0]
    cursor.execute('select count(*) from '+table_name+';')
    (number_of_rows,) = cursor.fetchone()

    # parse null value to `0`
    def nullify(csv_row):
        return list(map(lambda row: '0' if row == "" else row, csv_row.split(',')))

    # Check if done migration
    print(emoji.emojize(':airplane: Starting to migrate '+table_name))
    if number_of_rows == 0:
        for i in range(1, len(csv)):
            insert_query = "insert into " + table_name + " (" + csv_header.replace('"', '') + ")"
            csv_data = ', '.join(nullify(csv[i]))
            values = " values (" + csv_data + ")"
            sql = insert_query+values
            # print(sql)
            # sql = mdb.escape_string(insert_query+values)
            cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
            cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()
print(emoji.emojize(':thumbs_up: Done migrating '+table_name))
