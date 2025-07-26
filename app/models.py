# app/models.py
from beanie import Document, Link
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

# Definição do Enum com as opções permitidas
class TipoAkumaNoMi(str, Enum):
    PARAMECIA = "Paramecia"
    ZOAN = "Zoan"
    LOGIA = "Logia"

class Personagem(Document):
    nome: str
    bando: Optional[str] = "Desconhecido"
    recompensa: Optional[int] = 0
    descricao: Optional[str] = ""

    class Settings:
        name = "personagens"

class NiveisPoder(BaseModel):
    dominio_basico: Optional[List[str]] = []
    aplicacoes_avancadas: Optional[dict] = {}
    despertar: Optional[dict] = {"status": "Não despertada", "descricao": ""}

# --- MOLDE DO BANCO DE DADOS ---
class AkumaNoMi(Document):
    nome_romanizado: str
    nome_br: str
    tipo: TipoAkumaNoMi
    usuario_atual: Optional[Link[Personagem]] = None
    descricao: str
    niveis_de_poder: NiveisPoder
    imagem_url: Optional[str] = None

    class Settings:
        name = "akuma_no_mi"

# --- MOLDE APENAS PARA CRIAR UMA FRUTA (ENTRADA) ---
class AkumaNoMiCreate(BaseModel):
    nome_romanizado: str
    nome_br: str
    tipo: TipoAkumaNoMi
    descricao: str
    niveis_de_poder: NiveisPoder
    imagem_url: Optional[str] = None

# --- MOLDE DE SAÍDA (RESPOSTA) ---
class AkumaNoMiRead(BaseModel):
    nome_romanizado: str
    nome_br: str
    tipo: TipoAkumaNoMi
    descricao: str
    niveis_de_poder: NiveisPoder
    imagem_url: Optional[str] = None
    usuario_atual: Optional[Personagem] = None

    class Config:
        from_attributes = True