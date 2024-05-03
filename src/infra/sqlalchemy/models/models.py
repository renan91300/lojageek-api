from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base


class Product(Base):#Define uma classe chamada Product que herda da classe Base, 
                    #O que significa que Product será um modelo de dados SQLAlchemy.

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True )
    sku = Column(String)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    unit_type = Column(String)
    category = Column(String)
    weight = Column(Float)
    width = Column(Float)
    height = Column(Float)
    length = Column(Float)
    qty_items_per_box = Column(Integer)
    ean = Column(String)
    promo = Column (Boolean)
    promo_discount = Column(Float)
    qty_stock = Column(Integer)


class Client(Base):#Define uma classe chamada Client que herda da classe Base, 
                    #O que significa que Client será um modelo de dados SQLAlchemy.

    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True )
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    phone = Column(String)
    cpf = Column(String)


class Supplier(Base):
    __tablename__ = "supplier"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String)
    company_name = Column(String)
    contact_name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    
