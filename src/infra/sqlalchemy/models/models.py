from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Product(Base):#Define uma classe chamada Product que herda da classe Base, 
                    #O que significa que Product será um modelo de dados SQLAlchemy.

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True )
    sku = Column(String)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    size_weight = Column(Float)
    size_width = Column(Float)
    size_height = Column(Float)
    size_length = Column(Float)
    qty_items_per_box = Column(Integer)
    ean = Column(String)
    promo = Column (Boolean)
    promo_discount = Column(Float)
    qty_stock = Column(Integer)

    category_id = Column(Integer, ForeignKey('category.id', name="fk_product_category"))
    category = relationship("Category", back_populates="products")

    order_items = relationship("OrderItem", back_populates="product")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True )
    name = Column(String)
    
    products = relationship("Product", back_populates="category")


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True )
       
    client_id = Column(Integer, ForeignKey("client.id", name="fk_order_client"))
    client = relationship("Client", back_populates="orders")

    order_items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True, index=True )
       
    order_id = Column(Integer, ForeignKey("order.id", name="fk_order_item_order"))
    order = relationship("Order", back_populates="order_items")
       
    product_id = Column(Integer, ForeignKey("product.id", name="fk_order_item_product"))
    product = relationship("Product", back_populates="order_items")


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

    orders = relationship("Order", back_populates="client")


class Supplier(Base):
    __tablename__ = "supplier"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String)
    company_name = Column(String)
    contact_name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    
