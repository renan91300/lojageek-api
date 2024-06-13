from sqlalchemy import update
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


    def update(self, client: schemas.Client):
        db_client = self.db.query(models.Client).filter(models.Client.id == client.id).first() is not None

        if db_client:
            update_stmt = update(models.Client).where(
                models.Client.id == client.id
            ).values(
                first_name=client.first_name, 
                last_name=client.last_name,
                email=client.email,
                password=client.password,
                address=client.address,
                phone=client.phone,
                cpf=client.cpf
            )

            self.db.execute(update_stmt)
            self.db.commit()

            return  True
        raise ValueError('ID do cliente não encontrado.')
    

    def delete(self, client_id: int):
        clients_with_order = self.db.query(models.Order).filter(models.Order.client_id == client_id).first()

        if clients_with_order:
            raise ValueError('Não é possível deletar o cliente pois há pedidos associados à ele.')

        db_client = self.db.query(models.Client).filter(models.Client.id == client_id).first()

        if db_client:
            self.db.delete(db_client)
            self.db.commit()
            
            return True
        raise ValueError('ID do cliente não encontrado.')
