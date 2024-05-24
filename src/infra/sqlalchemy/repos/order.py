from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session, joinedload
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


    def read(self):
        orders = self.db.query(models.Order).options(joinedload(models.Order.order_items)).all()
        return  orders
    
    def update(self, order: schemas.Order):   
        delete_stmt = delete(models.OrderItem).filter(models.OrderItem.order_id == order.id)
        self.db.execute(delete_stmt)
        
        update_stmt = update(models.Order).where(
            models.Order.id == order.id
        ).values(
            client_id = order.client_id,

        )

        for item in order.items:
            if not self.product_exists(item):
                raise ValueError('Product not found')
            
            order_item = models.OrderItem(order_id=order.id, product_id=item)
            self.db.add(order_item)

        self.db.execute(update_stmt)
        self.db.commit()

        return  order
    
    def delete(self, order_id: int):
        # db_order = self.db.query(models.Order).filter(models.Order.id == order_id).first()
        delete_items_stmt = delete(models.OrderItem).filter(models.OrderItem.order_id == order_id)
        delete_order_stmt = delete(models.Order).filter(models.Order.id == order_id)

        self.db.execute(delete_items_stmt)
        order_deleted = self.db.execute(delete_order_stmt)        
        self.db.commit()
        if order_deleted.rowcount > 0:
            return True
        return False