import MySQLdb as mdb

conn = mdb.connect('localhost', 'root', 'root', 'chuchudb')
cursor = conn.cursor()

with open('data/states.csv', 'r') as state:
    lines = state.read().splitlines()
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        print(row)
        # cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
        # cursor.execute(
        #     "INSERT INTO state (abbreviation, name, usps) VALUES ('%s', '%s', '%s');" %
        #     ("HK", "Eighty 8", 0)
        # )

cursor.close()
conn.commit()
conn.close()
