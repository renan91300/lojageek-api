from pydantic import BaseModel
from typing import Optional, List


class Client(BaseModel):
    id: Optional[str] = None
    first_name: str
    last_name: str
    email: str
    password: str
    address: str
    phone: str
    cpf: str

class Product(BaseModel):
    id: Optional[str] = None
    sku: str
    name: str
    description: str
    price: float
    unit_type: str
    category: str
    weight: float
    width: float
    height: float
    length: float
    qty_items_per_box: int
    ean: str
    promo: bool = False
    promo_discount: Optional[float] = 0.00
    qty_stock: int

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = False
    endereco: str
    observacoes: Optional[str] = "Sem Observações"
