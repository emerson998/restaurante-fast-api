from fastapi import FastAPI
from app.api.v1.routes import router
from app.infra.database import Base, engine

# Cria tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
