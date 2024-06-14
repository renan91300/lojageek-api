from sqlalchemy import update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepoProduct():

    def __init__(self, db: Session):
        self.db = db
        


    def category_exists(self, category_id: int):
        return self.db.query(models.Category).filter(models.Category.id == category_id).first() is not None


    def create(self, product: schemas.Product):# Covertendo o Schema em um modelo
        if not self.category_exists(product.category_id):
            raise ValueError('Categoria não encontrada')

        db_product = models.Product(
            sku=product.sku, 
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id,
            size_weight=product.size_weight,
            size_width=product.size_width,
            size_height=product.size_height,
            size_length=product.size_length,
            qty_items_per_box=product.qty_items_per_box,
            ean=product.ean,
            promo=product.promo,
            promo_discount = product.promo_discount if product.promo and product.promo_discount is not None else 0.00,
            qty_stock=product.qty_stock
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product


    def read(self):
        products = self.db.query(models.Product).all()
        return  products


    def update(self, product: schemas.Product):
        db_product = self.db.query(models.Product).filter(models.Product.id == product.id).first() is not None

        if db_product:
            update_stmt = update(models.Product).where(
                models.Product.id == product.id
            ).values(
                sku=product.sku,
                name=product.name,
                description=product.description,
                price=product.price,
                category_id=product.category_id,
                size_weight=product.size_weight,
                size_width=product.size_width,
                size_height=product.size_height,
                size_length=product.size_length,
                qty_items_per_box=product.qty_items_per_box,
                ean=product.ean,
                promo=product.promo,
                promo_discount=product.promo_discount,
                qty_stock=product.qty_stock
            )

            self.db.execute(update_stmt)
            self.db.commit()

            return True
        raise ValueError('ID do produto não encontrado.')
    

    def delete(self, product_id: int):
        product_associated = self.db.query(models.OrderItem).filter(models.OrderItem.product_id == product_id).first()
        
        if product_associated:
            raise ValueError('Não é possível excluir o produto, pois está associado a um pedido.')
        
        db_product = self.db.query(models.Product).filter(models.Product.id == product_id).first()
        
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
            return True
        raise ValueError('ID do produto não encontrado.')