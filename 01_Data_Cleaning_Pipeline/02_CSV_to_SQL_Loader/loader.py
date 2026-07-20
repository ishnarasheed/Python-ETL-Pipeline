import sqlite3
import pandas as pd

def load_to_sql(csv_file, db_name, table_name):
    # CSV file read karna
    df = pd.read_csv(csv_file)
    
    # Database connection banana
    conn = sqlite3.connect(db_name)
    
    # Data ko SQL table mein save karna
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    conn.close()
    print(f"Data successfully loaded into {table_name} table.")

# Example usage:
# load_to_sql('data.csv', 'my_database.db', 'users')
