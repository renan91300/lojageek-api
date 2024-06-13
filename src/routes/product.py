from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..schemas.schemas import Product
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repos.product import RepoProduct


router = APIRouter()

# Product
#   create
@router.post('/product')
def create_product(product: Product, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    try:
        product_created = RepoProduct(db).create(product)
        return {'status': 200, 'response': 'Produto criado com sucesso.'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}

#   read
@router.get('/product')
def list_products(db:Session = Depends(get_db)):
    products_list = RepoProduct(db).read()
    return {'status': 200, 'response': products_list}

#   update
@router.put('/product')
def update_product(product: Product, db:Session = Depends(get_db)):
    product_updated = RepoProduct(db).update(product)
    
    if product_updated:
        return {'status': 200, 'response': 'Produto atualizado com sucesso.'}

    return {'status': 400, 'response': 'Erro - Não foi possível atualizar o produto'}

#   delete
@router.delete('/product/{product_id}')
def delete_product(product_id: int, db:Session = Depends(get_db)):
    product_deleted = RepoProduct(db).delete(product_id)

    if product_deleted:
        return {'status': 200, 'response': 'Produto deletado com sucesso.'}

    return {'status': 400, 'response': 'Erro - Não foi possível deletar o produto'}