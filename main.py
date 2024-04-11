from fastapi import FastAPI, File, UploadFile, Response, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel, Field #Modelos Bases para os objetos das requisições

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


class Product(BaseModel): #Herança de BaseMOdel
    id: int = Field(None)
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
    promo: bool
    promo_discount: Optional[float]
    qty_stock: int
    
products: List[Product] = []
product_next_id = 1


#class Address(BaseModel) - todo

class Client(BaseModel):
    id: int = Field(None)
    first_name: str
    last_name: str
    email: str
    password: str
    address: str
    phone: str
    cpf: str

clients: List[Client] = []
client_next_id = 1


# Get all Products
@app.get('/product')
def list_products():
    return products


# Get Product by id
@app.get('/product/{product_id}')
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"status": 404, "response": "Product not found"}


# Create Product
@app.post('/product')
def create_product(product: Product):
    global product_next_id
    product.id = product_next_id
    product_next_id += 1
    products.append(product)
    return {"status": 200, "response": "Product successfully created"}


# Delete Product
@app.delete('/product/{product_id}')
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            products.pop(index)
            return {"status": 200, "response": "Product successfully deleted"}
    return {"status": 404, "response": "Product not found"}


# Get all Clients
@app.get('/client')
def list_clients():
    return {"status": 200, "response": clients}


# Get Client by id
@app.get('/client/{client_id}')
def get_client_by_id(client_id: int):
    for client in clients:
        if client.id == client_id:
            return client
    return {"status": 404, "response": "Client not found"}


# Create Client
@app.post('/client')
def create_client(client: Client):
    global client_next_id
    client.id = client_next_id
    client_next_id += 1
    clients.append(client)
    return {"status": 200, "response": "Client successfully created"}


# Delete Client
@app.delete('/client/{client_id}')
def delete_client(client_id: int):
    for index, client in enumerate(clients):
        if client.id == client_id:
            clients.pop(index)
            return {"status": 200, "response": "Client successfully deleted"}
    return {"status": 404, "response": "Client not found"}
