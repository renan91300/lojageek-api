from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import create_db
from src.routes import category, client, order, product, supplier

create_db()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(category.router)

app.include_router(client.router)

app.include_router(order.router)

app.include_router(product.router)

app.include_router(supplier.router)
