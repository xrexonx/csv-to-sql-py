import MySQLdb as mdb

PRICE     = 0
TIMESTAMP = 1
SOURCE    = 2

conn = mdb.connect('hostname', 'username', 'p@s$w0rd', 'database')
cursor = conn.cursor()

with open('gold_price.csv', 'r') as gold_prices:
    lines = gold_prices.read().splitlines()

    for i in range(1, len(lines)):
        _tuple = lines[i].split(',')
        cursor.execute("INSERT INTO gold_price (price, time, source) VALUES (%s, '%s', '%s');" %
        (_tuple[PRICE], _tuple[TIMESTAMP], _tuple[SOURCE]))

cursor.close()
conn.commit()
conn.close()
