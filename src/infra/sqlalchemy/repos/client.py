from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepoClient():

    def __init__(self, db: Session):
        self.db = db
        


    def create(self, client: schemas.Client):# Covertendo o Schema em um modelo
        db_client = models.Client(
            first_name=client.first_name, 
            last_name=client.last_name,
            email=client.email,
            password=client.password,
            address=client.address,
            phone=client.phone,
            cpf=client.cpf
        )
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)
        return db_client


    def read(self):
        clients = self.db.query(models.Client).all()
        return  clients


    def delete(self, client_id: int):
        db_client = self.db.query(models.Client).filter(models.Client.id == client_id).first()

        if db_client:
            self.db.delete(db_client)
            self.db.commit()
            return True
        return False