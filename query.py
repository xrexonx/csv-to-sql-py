import MySQLdb as mdb

conn = mdb.connect('localhost', 'root', 'root', 'chuchudb')
cursor = conn.cursor()

cursor.execute('SELECT * FROM company;')
states = cursor.fetchone()

if states:
    print(states)
else:
    print('No record found')
# for row in states:
#     print(row)

cursor.close()
conn.close()

# https://jasonfavrod.com/mysql-and-python3/
