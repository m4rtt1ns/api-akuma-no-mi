# app/models.py
from beanie import Document
from pydantic import BaseModel
from typing import List, Optional

class NiveisPoder(BaseModel):
    dominio_basico: Optional[List[str]] = []
    aplicacoes_avancadas: Optional[dict] = {}
    despertar: Optional[dict] = {"status": "Não despertada", "descricao": ""}

class AkumaNoMi(Document):
    nome_romanizado: str
    nome_br: str
    tipo: str
    usuario_atual: Optional[str] = None
    descricao: str
    niveis_de_poder: NiveisPoder
    imagem_url: Optional[str] = None

    class Settings:
        name = "akuma_no_mi" # Nome da coleção no banco de dados