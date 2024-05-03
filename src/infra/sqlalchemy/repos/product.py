from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepoProduct():

    def __init__(self, db: Session):
        self.db = db
        


    def create(self, product: schemas.Product):# Covertendo o Schema em um modelo
        db_product = models.Product(sku=product.sku, 
                                    name=product.name,
                                    description=product.description,
                                    price=product.price,
                                    unit_type=product.unit_type,
                                    category=product.category,
                                    weight=product.weight,
                                    width=product.width,
                                    height=product.height,
                                    length=product.length,
                                    qty_items_per_box=product.qty_items_per_box,
                                    ean=product.ean,
                                    promo=product.promo,
                                    promo_discount=product.promo_discount,
                                    qty_stock=product.qty_stock)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product


    def read(self):
        products = self.db.query(models.Product).all()
        return  products

    def delete(self, product_id: int):
        db_product = self.db.query(models.Product).filter(models.Product.id == product_id).first()

        if db_product:
            self.db.delete(db_product)
            self.db.commit()
            return True
        return False