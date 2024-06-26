from pydantic import BaseModel
from typing import Optional, List


class Product(BaseModel):
    id: Optional[int] = 0
    sku: str
    name: str
    description: str
    price: float
    category_id: int
    size_weight: float
    size_width: float
    size_height: float
    size_length: float
    qty_items_per_box: int
    ean: str
    promo: bool = False
    promo_discount: float = 0.00
    qty_stock: int

    class Config:
        orm_mode = True


class Category(BaseModel):
    id: Optional[int] = 0
    name: str

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[int] = 0
    client_id: int
    items: List[int]

    class Config:
        orm_mode = True


class Client(BaseModel):
    id: Optional[int] = 0
    first_name: str
    last_name: str
    email: str
    password: str
    address: str
    phone: str
    cpf: str


class Supplier(BaseModel):
    id: Optional[int] = 0
    cnpj: str
    company_name: str
    contact_name: str
    email: str
    phone: str
    address: str
