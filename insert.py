# import os
import MySQLdb as mdb

conn = mdb.connect('localhost', 'root', 'root', 'chuchudb')
cursor = conn.cursor()

table_name = 'county'

with open('data/'+table_name+'.csv', 'r') as state:
    csv = state.read().splitlines()
    csv_header = csv[0]
    cursor.execute('SELECT * FROM '+table_name+';')
    # db_name = os.getenv("DB_NAME")
    # print(db_name)
    # print(os.listdir("data"))

    # for x in os.listdir('data'):
    #     print(x)

    # Check if done migration
    if not cursor.fetchone():
        for i in range(1, len(csv)):
            insert_query = "insert into " + table_name + " (" + csv_header.replace('"', '') + ")"
            values = " values (" + csv[i] + ")"
            sql = insert_query + values
            # print(sql)
            cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
            cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()
print("Done migrating "+table_name)
