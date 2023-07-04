from sqlalchemy import Column, Integer, String, Table, create_engine,MetaData

DB_URL = 'sqlite:///college.db'
ENGINE = create_engine(DB_URL , echo=True)
meta = MetaData()

user = Table('user',meta,
             Column('id',Integer,primary_key=True),
             Column('name',String(50)),
             Column('password',String(50)) 
             )
s = user.select()

conn = ENGINE.connect()
result = conn.execute(s)

for row in result :
    print(row)