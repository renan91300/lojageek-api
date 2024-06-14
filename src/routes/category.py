from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..schemas.schemas import Category
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repos.category import RepoCategory


router = APIRouter()

# Category

#   create
@router.post('/category')
def create_category(category: Category, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    category_created = RepoCategory(db).create(category)
    
    if category_created:
        return {'status': 200, 'response': 'Categoria criada com sucesso'}

    return {'status': 400, 'response': 'Erro - Não Foi possível criar a categoria'}


#   read
@router.get('/category')
def list_categories(db:Session = Depends(get_db)):
    categories_list = RepoCategory(db).read()
    return {'status': 200, 'response': categories_list}


#   update
@router.put('/category')
def update_category(category: Category, db:Session = Depends(get_db)):
    try:
        category_updated = RepoCategory(db).update(category)
    
        if category_updated:
            return {'status': 200, 'response': 'Categoria atualizada com sucesso.'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}
    
    return {'status': 400, 'response': 'Erro - Não foi possível atualizar a categoria'}


#   delete
@router.delete('/category/{category_id}')
def delete_category(category_id: int, db: Session = Depends(get_db)):
    try:
        category_deleted = RepoCategory(db).delete(category_id)
        if category_deleted:
            return {'status': 200, 'response': 'Categoria deletada com sucesso'}
    except ValueError as ve:
        return {'status': 400, 'response': str(ve)}

    return {'status': 400, 'response': 'Erro - Não Foi possível excluir a categoria'}