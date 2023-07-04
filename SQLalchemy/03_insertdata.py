from sqlalchemy import Column, Integer, String, Table, create_engine,MetaData
from sqlalchemy.sql import text

DB_URL = 'sqlite:///college.db'
ENGINE = create_engine(DB_URL , echo=True)

meta = MetaData()

user = Table('user',meta,
             Column('id',Integer,primary_key=True),
             Column('name',String(50)),
             Column('password',String(50)) 
             )

meta.create_all(ENGINE)


# s = text("insert into user (id,name,password) values (1,'Ajith','123456'),(2,'Vinoth','g7t3hdi'),(3,'Ram','g67t38d')")
s = user.insert().values({'id':1,'name':'Manoj','password':'bjdguy3'})

conn = ENGINE.connect()
conn.execute(s)

# ins = user.insert().values([
#                     {'name':'Ajith','password':'123456'},
#                     {'name':'Ram','password':'2345'},
#                     {'name':'Bala','password':'6472'},
#                     {'name':'Vinay','password':'u743893'},
#                     {'name':'Ashok','password':'u3788d'}])

# result = conn.execute(ins)

  