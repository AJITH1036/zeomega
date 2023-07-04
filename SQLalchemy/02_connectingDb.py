from sqlalchemy import create_engine

DB_URL = 'sqlite:///college.db'
ENGINE = create_engine(DB_URL)

conn = ENGINE.connect()

try :
    print(f"connection is OK with {conn}")
except:
    print("connection failed")
