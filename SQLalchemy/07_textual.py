from sqlalchemy import Table,Column,Integer,String,MetaData, text,create_engine
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

Session = sessionmaker(bind = engine)
session = Session()


for cust in session.query(Customers).filter(text("id<4")) :
    print(cust.name)

for cust in session.query(Customers).from_statement(text("Select * from customers")).all() :
    print(cust.id,cust.name,cust.email)
