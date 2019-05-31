import MySQLdb as mdb

conn = mdb.connect('localhost', 'root', 'root', 'chuchudb')
cursor = conn.cursor()

cursor.execute('SELECT * FROM state;')
states = cursor.fetchall()
for row in states:
    print(row)

cursor.close()
conn.close()

# https://jasonfavrod.com/mysql-and-python3/
