import os
import Migration as db
from dotenv import load_dotenv
load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

# TODO: Add DB exist config checking

csv_files = os.listdir('data')
if len(csv_files) > 0:
    # [print(table_name) for table_name in csv_files]
    # migration = db.Migration('localhost', 'root', 'root', 'chuchudb')
    migration = db.Migration(db_host, db_user, db_pass, db_name)
    [migration.run_query(table_name) for table_name in csv_files]



