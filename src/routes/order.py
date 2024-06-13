from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..schemas.schemas import Order
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repos.order import RepoOrder

router = APIRouter()

# Order 
#   read
@router.get('/order')
def list_orders(db:Session = Depends(get_db)):
    orders_list = RepoOrder(db).read()
    return {'status': 200, 'response': orders_list}


#   create
@router.post('/order')
def create_order(order: Order, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    try:
        order_created = RepoOrder(db).create(order)
        return {'status': 200, 'response': 'Pedido criado com sucesso.'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}
    

#   update
@router.put('/order')
def update_order(order: Order, db:Session = Depends(get_db)):
    try:
        order_updated = RepoOrder(db).update(order)
    
        if order_updated:
            return {'status': 200, 'response': 'Pedido atualizado com sucesso.'}

        return {'status': 400, 'response': 'Erro - Não foi possível atualizar o pedido'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}


#   delete
@router.delete('/order/{order_id}')
def delete_order(order_id: int, db:Session = Depends(get_db)):
    order_deleted = RepoOrder(db).delete(order_id)

    if order_deleted:
        return {'status': 200, 'response': 'Pedido deletado com sucesso.'}

    return {'status': 400, 'response': 'Erro - Não foi possível deletar o pedido'}
