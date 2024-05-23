from sqlalchemy import update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepoOrder():

    def __init__(self, db: Session):
        self.db = db
        


    def client_exists(self, client_id: int):
        return self.db.query(models.Client).filter(models.Client.id == client_id).first() is not None


    def product_exists(self, product_id: int):
        return self.db.query(models.Product).filter(models.Product.id == product_id).first() is not None


    def create(self, order: schemas.Order):# Covertendo o Schema em um modelo
        if not self.client_exists(order.client_id):
            raise ValueError('Client not found')

        db_order = models.Order(client_id=order.client_id)
        self.db.add(db_order)
        self.db.flush()

        for item in order.items:
            if not self.product_exists(item):
                raise ValueError('Product not found')
            
            order_item = models.OrderItem(order_id=db_order.id, product_id=item)
            self.db.add(order_item)

        self.db.commit()
        self.db.refresh(db_order)
        return db_order
