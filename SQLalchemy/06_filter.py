from sqlalchemy import Table,Column,Integer,String,MetaData,create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sales.db',echo=True)
Base = declarative_base()

class Customers(Base) :
    __tablename__ = 'customers'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

# Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_

Session = sessionmaker(bind = engine)
session = Session()

result = session.query(Customers).filter(or_(Customers.id.in_([1,4]),Customers.name.like('A%')))

for row in result :
    print(row.name , row.address , row.email)