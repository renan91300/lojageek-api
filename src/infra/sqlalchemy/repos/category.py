from sqlalchemy import update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepoCategory():

    def __init__(self, db: Session):
        self.db = db
        


    def create(self, category: schemas.Category):# Covertendo o Schema em um modelo
        db_category = models.Category(name=category.name)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

 
    def read(self):
        categories = self.db.query(models.Category).all()
        return  categories


    def update(self, category: schemas.Category):
        db_category = self.db.query(models.Category).filter(models.Category.id == category.id).first() is not None

        if db_category: 
            update_stmt = update(models.Category).where(
                models.Category.id == category.id
            ).values(
                name=category.name
            )

            self.db.execute(update_stmt)
            self.db.commit()

            return True
        raise ValueError('ID da categoria não encontrado.')


    def delete(self, category_id: int):
        products_with_category = self.db.query(models.Product).filter(models.Product.category_id == category_id).first()

        if products_with_category:
            raise ValueError('Não é possível excluir a categoria pois há produtos associados à ela.')

        db_category = self.db.query(models.Category).filter(models.Category.id == category_id).first()

        if db_category:
            self.db.delete(db_category)
            self.db.commit()
            return True
        raise ValueError('ID da categoria não encontrado.')