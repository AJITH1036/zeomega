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

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

# c1 = Customers(name = 'Ajith',address = 'Chennai',email='ajith@c.com')
# session.add(c1)

c2 = [Customers(name = 'Ram',address = 'bangalore',email='ram@c.com'),
      Customers(name = 'Mahesh',address = 'Mysore',email='mahesh@c.com'),
      Customers(name = 'Dinoj',address = 'Mumbai',email='dinoj@c.com')]

session.add_all(c2)
session.commit()

result = session.query(Customers).get(2)
print(result.name,result.email,result.address)

# for row in result :
#     print(row.name , row.address , row.email)

