import pytest
import asyncio
from httpx import AsyncClient
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

# Importamos nosso app FastAPI e os modelos do projeto principal
from app.main import app
from app.models import AkumaNoMi, Personagem
from app.config import settings

@pytest.fixture(scope="session")
def event_loop():
    """
    Cria uma instância do loop de eventos para toda a sessão de testes.
    É uma configuração técnica necessária para o pytest-asyncio.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_db_client():
    """
    Esta é a nossa grande mágica! Esta função executa apenas uma vez por sessão.
    """
    # 1. Define um nome diferente para o banco de dados de teste
    test_db_name = "akuma_db_test"
    client = AsyncIOMotorClient(settings.MONGO_DATABASE_URL)

    # 2. Inicializa o Beanie para usar esse banco de dados de teste
    await init_beanie(
        database=client[test_db_name],
        document_models=[AkumaNoMi, Personagem],
    )

    print(f"\n--- CONECTADO ao banco de dados de teste: {test_db_name} ---")

    # 3. Disponibiliza o cliente para os testes usarem
    yield client

    # 4. DEPOIS QUE TODOS OS TESTES TERMINAREM, apaga o banco de dados de teste
    print(f"\n--- LIMPANDO o banco de dados de teste: {test_db_name} ---")
    await client.drop_database(test_db_name)
    client.close()

@pytest.fixture(scope="function")
async def test_client(test_db_client):
    """
    Cria um "navegador de teste" para fazer requisições à nossa API.
    Esta função executa para CADA teste, garantindo isolamento.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client