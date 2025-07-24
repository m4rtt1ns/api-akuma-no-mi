# app/config.py
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Define um "molde" para as nossas configurações
class Settings:
    MONGO_DATABASE_URL: str = os.getenv("MONGO_DATABASE_URL")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")

# ===================================================================
# !! ESTA É A LINHA MAIS IMPORTANTE E QUE PROVAVELMENTE FALTA !!
# Aqui nós criamos a variável 'settings' (minúsculo) a partir 
# da classe 'Settings' (maiúsculo) para que outros arquivos possam usá-la.
settings = Settings()
# ===================================================================