import MySQLdb as mdb

conn = mdb.connect('localhost', 'root', 'root', 'chuchudb')
cursor = conn.cursor()

with open('data/state.csv', 'r') as dmas:
    lines = dmas.read().splitlines()
    for i in range(1, len(lines)):
        # _tuple = lines[i].split(',')
        cursor.execute(
            "SET FOREIGN_KEY_CHECKS = 0; INSERT INTO state (abbreviation, name, usps) VALUES ('%s', '%s', '%s');" %
            ("HK", "Eighty 8", 0)
        )

cursor.close()
conn.commit()
conn.close()
