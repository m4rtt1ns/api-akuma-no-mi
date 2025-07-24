# app/main.py
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

# CORREÇÃO IMPORTANTE AQUI:
# Endereços completos para nossos módulos internos.
from app.config import settings
from app.models import AkumaNoMi
from app.routers import akuma_no_mi_router

# Cria a instância principal da aplicação
app = FastAPI(
    title="API de Akuma no Mi - One Piece",
    description="Uma API para consultar informações e poderes das Frutas do Diabo.",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_db_client():
    """Conecta ao banco de dados quando a API inicia."""
    client = AsyncIOMotorClient(settings.MONGO_DATABASE_URL)
    await init_beanie(database=client[settings.DATABASE_NAME], document_models=[AkumaNoMi])

# Inclui todas as rotas que definimos no nosso roteador
app.include_router(akuma_no_mi_router.router)

@app.get("/", tags=["Root"])
async def read_root():
    """Endpoint raiz para verificar se a API está no ar."""
    return {"message": "Bem-vindo à API de Akuma no Mi! Acesse /docs para ver a documentação."}