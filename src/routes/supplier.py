from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..schemas.schemas import Supplier
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repos.supplier import RepoSupplier


router = APIRouter()
 
# Supplier
#   create
@router.post('/supplier')
def create_supplier(supplier: Supplier, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    supplier_created = RepoSupplier(db).create(supplier)
    return {'status': 200, 'response': 'Fornecedor criado com sucesso.'}

#   read
@router.get('/supplier')
def list_suppliers(db:Session = Depends(get_db)):
    suppliers_list = RepoSupplier(db).read()
    return {'status': 200, 'response': suppliers_list}

#   update
@router.put('/supplier')
def update_supplier(supplier: Supplier, db:Session = Depends(get_db)):
    supplier_updated = RepoSupplier(db).update(supplier)
    
    if supplier_updated:
        return {'status': 200, 'response': 'Fornecedor atualizado com sucesso.'}

    return {'status': 400, 'response': 'Erro -  Não foi possível atualizar o fornecedor'}

#   delete
@router.delete('/supplier/{supplier_id}')
def delete_supplier(supplier_id: int, db:Session = Depends(get_db)):
    supplier_deleted = RepoSupplier(db).delete(supplier_id)

    if supplier_deleted:
        return {'status': 200, 'response': 'Fornecedor deletado com sucesso.'}

    return {'status': 400, 'response': 'Erro -  Não foi possível deletar o fornecedor'}