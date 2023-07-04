
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

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# for c,i in session.query(Customers,Invoice).filter(Customers.id == Invoice.custid).all() :
#     print(f"ID-{c.id} name : {c.name} Invoice No: {i.invno}  Amount : {i.amount}")

result = session.query(Customers).join(Invoice).filter(Invoice.amount == 890).all()

for row in result :
    for inv in row.invoices :
      print(f"ID-{row.id} name : {row.name} Invoice No: {inv.invno}  Amount : {inv.amount}")



