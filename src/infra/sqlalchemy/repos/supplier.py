from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepoSupplier():

    def __init__(self, db: Session):
        self.db = db
        


    def create(self, supplier: schemas.Supplier):# Covertendo o Schema em um modelo
        db_supplier = models.Supplier(
            cnpj=supplier.cnpj, 
            company_name=supplier.company_name,
            contact_name=supplier.contact_name,
            email=supplier.email,
            phone=supplier.phone,
            address=supplier.address
        )
        self.db.add(db_supplier)
        self.db.commit()
        self.db.refresh(db_supplier)
        return db_supplier


    def read(self):
        suppliers = self.db.query(models.Supplier).all()
        return  suppliers


    def delete(self, supplier_id: int):
        db_supplier = self.db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()

        if db_supplier:
            self.db.delete(db_supplier)
            self.db.commit()
            return True
        return False
