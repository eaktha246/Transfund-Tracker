import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def init_database():
    try:
        # Connect to default 'postgres' database first to create the 'mini' DB
        print("Connecting to PostgreSQL server to verify/create 'mini' database...")
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        
        # Check if database 'mini' exists
        cur.execute("SELECT 1 FROM pg_database WHERE datname='mini'")
        exists = cur.fetchone()
        
        if not exists:
            cur.execute("CREATE DATABASE mini")
            print("Database 'mini' created successfully!")
        else:
            print("Database 'mini' already exists.")
            
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error checking/creating database: {e}")

if __name__ == "__main__":
    init_database()
