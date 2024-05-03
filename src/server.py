from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas.schemas import Product, Client, Supplier
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repos.product import RepoProduct
from src.infra.sqlalchemy.repos.client import RepoClient
from src.infra.sqlalchemy.repos.supplier import RepoSupplier

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


# Create Supplier
@app.post('/supplier')
def create_supplier(supplier: Supplier, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    supplier_created = RepoSupplier(db).create(supplier)
    return {'status': 200, 'response': 'Supplier successfully created'}


@app.get('/supplier')
def list_suppliers(db:Session = Depends(get_db)):
    suppliers_list = RepoSupplier(db).read()
    return {'status': 200, 'response': suppliers_list}


@app.delete('/supplier/{supplier_id}')
def delete_supplier(supplier_id: int, db:Session = Depends(get_db)):
    suppliers_deleted = RepoSupplier(db).delete(supplier_id)

    if suppliers_deleted:
        return {'status': 200, 'response': 'Supplier successfully deleted'}

    return {'status': 400, 'response': 'Error - Unable to delete the Supplier'}
