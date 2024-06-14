from fastapi import  Depends, APIRouter
from sqlalchemy.orm import Session
from ..schemas.schemas import Client
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repos.client import RepoClient


router = APIRouter()

# Client
#   create
@router.post('/client')
def create_client(client: Client, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    client_created = RepoClient(db).create(client)
    
    if client_created:
        return {'status': 200, 'response': 'Cliente criado com sucesso.'}

    return {'status': 400, 'response': 'Erro - Não foi possível criar o cliente'}


#   read
@router.get('/client')
def list_clients(db:Session = Depends(get_db)):
    clients_list = RepoClient(db).read()
    return {'status': 200, 'response': clients_list}


#   update
@router.put('/client')
def update_client(client: Client, db:Session = Depends(get_db)):
    try:
        client_updated = RepoClient(db).update(client)
    
        if client_updated:
            return {'status': 200, 'response': 'Cliente atualizado com sucesso.'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}
    
    return {'status': 400, 'response': 'Erro - Não foi possível atualizar o cliente'}


#   delete
@router.delete('/client/{client_id}')
def delete_client(client_id: int, db:Session = Depends(get_db)):
    try:
        client_deleted = RepoClient(db).delete(client_id)
        if client_deleted:
            return {'status': 200, 'response': 'Cliente deletado com sucesso.'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}

    return {'status': 400, 'response': 'Erro - Não foi possível excluir o cliente'}