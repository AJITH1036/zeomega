
from sqlalchemy import ForeignKey, Table,Column,Integer,String,MetaData,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///sales.db',echo=True)
Base = declarative_base()

class Customers(Base) :
    __tablename__ = 'customers'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

class Invoice(Base) :
    __tablename__ = 'invoices'
    id = Column(Integer,primary_key=True)
    custid = Column(Integer,ForeignKey("customers.id"))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customers",back_populates="invoices")

Customers.invoices = relationship("Invoice",order_by= Invoice.id , back_populates="customer")   

Base.metadata.create_all(engine)

c1 =[Customers(name = "Vinay",address="Chennai",email="vinay@c.com",invoices =  [Invoice(invno=11,amount=567),Invoice(invno=15,amount=890)]),
     Customers(name = "Ajith",address="Mysore",email="ajith@c.com",invoices =  [Invoice(invno=12,amount=675),Invoice(invno=16,amount=265)])] 

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.add_all(c1)
session.commit()


