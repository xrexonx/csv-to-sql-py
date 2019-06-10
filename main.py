import os
import Migration as db
from dotenv import load_dotenv

# Load environment
load_dotenv()

ENV = os.getenv("ENV")
DATA_DIR = os.getenv("DATA_DIR")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

# TODO: Add DB exist config checking

csv_dir = DATA_DIR+'/'+ENV
csv_files = os.listdir(csv_dir)
if len(csv_files) > 0:
    migration = db.Migration(db_host, db_user, db_pass, db_name)
    [migration.run_query(table_name, csv_dir) for table_name in csv_files]

    # Close connection after insertion
    migration.db_close()



