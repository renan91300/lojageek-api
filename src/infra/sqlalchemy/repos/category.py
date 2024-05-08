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


    def delete(self, category_id: int):
        products_with_category = self.db.query(models.Product).filter(models.Product.category_id == category_id).first()

        if products_with_category:
            raise ValueError('Cannot delete category because there are products associated with it.')

        db_category = self.db.query(models.Category).filter(models.Category.id == category_id).first()

        if db_category:
            self.db.delete(db_category)
            self.db.commit()
            return True
        raise ValueError('Category ID not found.')