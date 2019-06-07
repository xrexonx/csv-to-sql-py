import os
import emoji
import MySQLdb as mdb
from dotenv import load_dotenv

conn = mdb.connect('localhost', 'root', 'root', 'chuchudb')
cursor = conn.cursor()

table_name = 'county'
load_dotenv()
with open('data/'+table_name+'.csv', 'r') as csv_file:
    csv = csv_file.read().splitlines()
    csv_header = csv[0]
    cursor.execute('select * from '+table_name+';')
    db_name = os.getenv("DB_NAME")
    print(db_name)
    # print(os.listdir("data"))
    # for x in os.listdir('data'):
    #     print(x)

    def nullify(csv_row):
        return list(map(lambda row: '0' if row == "" else row, csv_row.split(',')))

    # Check if done migration
    print(emoji.emojize(':airplane: Starting to migrate '+table_name))
    if not cursor.fetchone():
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
