import os
import csv
import cx_Oracle
from dotenv import load_dotenv
from db_schema import schema_fields

# Load environment
load_dotenv()

# Get new db schema fields
data = schema_fields()

ENV = os.getenv("ENV")
DATA_DIR = os.getenv("DATA_DIR")
db_instance = os.getenv("ORACLE_DB_CON")
print('Connecting to database '+db_instance)
con = cx_Oracle.connect(db_instance)
cursor = con.cursor()

for key, value in data.items():
    fields = list(value.values())[1]
    table_name = 'LIL_'+key
    key = 'ZIPCODE' if key == 'ZIP' else key
    key = 'DMA_NETWORK' if key == 'NETWORK' else key
    csv_dir = DATA_DIR+'/'+ENV+'/'+key+'.csv'
    csv_file = open(csv_dir, "w")
    writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
    cursor.execute('SELECT '+fields+' FROM '+table_name)
    print('Writing '+key+ ' data to '+csv_dir)
    writer.writerow([i[0] for i in cursor.description])
    for row in cursor:
        writer.writerow(row)

    print(' ==> Done writing ' + key + ' data to ' + csv_dir)
    csv_file.close()

print('Done exporting data to csv.')
cursor.close()
con.close()

