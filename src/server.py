from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas.schemas import Product, Client
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repos.product import RepoProduct
from src.infra.sqlalchemy.repos.client import RepoClient

create_db()


app = FastAPI()


# Create Product
@app.post('/product')
def create_product(product: Product, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    product_created = RepoProduct(db).create(product)
    return {'status': 200, 'response': 'Product successfully created'}


@app.get('/product')
def list_products(db:Session = Depends(get_db)):
    products_list = RepoProduct(db).read()
    return {'status': 200, 'response': products_list}


@app.delete('/product/{product_id}')
def delete_product(product_id: int, db:Session = Depends(get_db)):
    products_deleted = RepoProduct(db).delete(product_id)

    if products_deleted:
        return {'status': 200, 'response': 'Product successfully deleted'}

    return {'status': 400, 'response': 'Error - Unable to delete the Product'}


# Create Client
@app.post('/client')
def create_client(client: Client, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    client_created = RepoClient(db).create(client)
    return {'status': 200, 'response': 'Client successfully created'}


@app.get('/client')
def list_clients(db:Session = Depends(get_db)):
    clients_list = RepoClient(db).read()
    return {'status': 200, 'response': clients_list}


@app.delete('/client/{client_id}')
def delete_client(client_id: int, db:Session = Depends(get_db)):
    clients_deleted = RepoClient(db).delete(client_id)

    if clients_deleted:
        return {'status': 200, 'response': 'Client successfully deleted'}

    return {'status': 400, 'response': 'Error - Unable to delete the Client'}