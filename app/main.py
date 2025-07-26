from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from contextlib import asynccontextmanager # 1. Importamos uma nova ferramenta

from app.config import settings
from app.models import AkumaNoMi, Personagem
from app.routers import akuma_no_mi_router, personagem_router

# 2. Criamos a nossa função "lifespan" (ciclo de vida)
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Este código roda antes de a API começar e depois que ela terminar."""
    # Código que roda ANTES da aplicação iniciar
    print("Iniciando conexão com o banco de dados...")
    client = AsyncIOMotorClient(settings.MONGO_DATABASE_URL)
    await init_beanie(
        database=client[settings.DATABASE_NAME], 
        document_models=[AkumaNoMi, Personagem]
    )
    print("Conexão com o banco estabelecida.")

    yield # A API fica rodando aqui no meio

    # Código que roda DEPOIS que a aplicação encerrar
    print("Fechando conexão com o banco de dados...")
    client.close()

# 3. Passamos o lifespan para a aplicação principal
app = FastAPI(
    title="API de Akuma no Mi - One Piece",
    description="Uma API para consultar informações e poderes das Frutas do Diabo.",
    version="1.0.0",
    lifespan=lifespan # <--- AQUI
)

# A função @app.on_event("startup") não é mais necessária e foi removida.

# Incluímos nossos roteadores
app.include_router(akuma_no_mi_router.router)
app.include_router(personagem_router.router)

# Nosso endpoint raiz
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bem-vindo à API de Akuma no Mi! Acesse /docs para ver a documentação."}