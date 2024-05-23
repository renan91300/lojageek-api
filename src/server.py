from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .schemas.schemas import Product, Client, Supplier, Category, Order
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.infra.sqlalchemy.repos.product import RepoProduct
from src.infra.sqlalchemy.repos.client import RepoClient
from src.infra.sqlalchemy.repos.category import RepoCategory
from src.infra.sqlalchemy.repos.supplier import RepoSupplier
from src.infra.sqlalchemy.repos.order import RepoOrder

create_db()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Category
#   create
@app.post('/category')
def create_category(category: Category, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    category_created = RepoCategory(db).create(category)
    
    if category_created:
        return {'status': 200, 'response': 'Category successfully created'}

    return {'status': 400, 'response': 'Error - Unable to create the Category'}

#   read
@app.get('/category')
def list_categories(db:Session = Depends(get_db)):
    categories_list = RepoCategory(db).read()
    return {'status': 200, 'response': categories_list}

#   delete
@app.delete('/category/{category_id}')
def delete_category(category_id: int, db: Session = Depends(get_db)):
    try:
        category_deleted = RepoCategory(db).delete(category_id)
        if category_deleted:
            return {'status': 200, 'response': 'Category successfully deleted'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}

    return {'status': 400, 'response': 'Error - Unable to delete the Category'}


# Product
#   create
@app.post('/product')
def create_product(product: Product, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    try:
        product_created = RepoProduct(db).create(product)
        return {'status': 200, 'response': 'Product successfully created'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}

#   read
@app.get('/product')
def list_products(db:Session = Depends(get_db)):
    products_list = RepoProduct(db).read()
    return {'status': 200, 'response': products_list}

#   update
@app.put('/product')
def update_product(product: Product, db:Session = Depends(get_db)):
    product_updated = RepoProduct(db).update(product)
    
    if product_updated:
        return {'status': 200, 'response': 'Product successfully updated'}

    return {'status': 400, 'response': 'Error - Unable to update the Product'}

#   delete
@app.delete('/product/{product_id}')
def delete_product(product_id: int, db:Session = Depends(get_db)):
    product_deleted = RepoProduct(db).delete(product_id)

    if product_deleted:
        return {'status': 200, 'response': 'Product successfully deleted'}

    return {'status': 400, 'response': 'Error - Unable to delete the Product'}


# Client
#   create
@app.post('/client')
def create_client(client: Client, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    client_created = RepoClient(db).create(client)
    
    if client_created:
        return {'status': 200, 'response': 'Client successfully created'}

    return {'status': 400, 'response': 'Error - Unable to create the Client'}

#   read
@app.get('/client')
def list_clients(db:Session = Depends(get_db)):
    clients_list = RepoClient(db).read()
    return {'status': 200, 'response': clients_list}

#   update
@app.put('/client')
def update_client(client: Client, db:Session = Depends(get_db)):
    client_updated = RepoClient(db).update(client)
    
    if client_updated:
        return {'status': 200, 'response': 'Client successfully updated'}

    return {'status': 400, 'response': 'Error - Unable to update the Client'}

#   delete
@app.delete('/client/{client_id}')
def delete_client(client_id: int, db:Session = Depends(get_db)):
    client_deleted = RepoClient(db).delete(client_id)

    if client_deleted:
        return {'status': 200, 'response': 'Client successfully deleted'}

    return {'status': 400, 'response': 'Error - Unable to delete the Client'}


# Supplier
#   create
@app.post('/supplier')
def create_supplier(supplier: Supplier, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    supplier_created = RepoSupplier(db).create(supplier)
    return {'status': 200, 'response': 'Supplier successfully created'}

#   read
@app.get('/supplier')
def list_suppliers(db:Session = Depends(get_db)):
    suppliers_list = RepoSupplier(db).read()
    return {'status': 200, 'response': suppliers_list}

#   update
@app.put('/supplier')
def update_supplier(supplier: Supplier, db:Session = Depends(get_db)):
    supplier_updated = RepoSupplier(db).update(supplier)
    
    if supplier_updated:
        return {'status': 200, 'response': 'Supplier successfully updated'}

    return {'status': 400, 'response': 'Error - Unable to update the Supplier'}

#   delete
@app.delete('/supplier/{supplier_id}')
def delete_supplier(supplier_id: int, db:Session = Depends(get_db)):
    supplier_deleted = RepoSupplier(db).delete(supplier_id)

    if supplier_deleted:
        return {'status': 200, 'response': 'Supplier successfully deleted'}

    return {'status': 400, 'response': 'Error - Unable to delete the Supplier'}


# Order
#   create
@app.post('/order')
def create_order(order: Order, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    try:
        order_created = RepoOrder(db).create(order)
        return {'status': 200, 'response': 'Order successfully created'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}