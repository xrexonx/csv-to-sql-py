import MySQLdb as mdb

conn = mdb.connect('localhost', 'root', 'root', 'chuchudb')
cursor = conn.cursor()

cursor.execute('SELECT * FROM state;')

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()

# https://jasonfavrod.com/mysql-and-python3/
