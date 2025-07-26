# app/routers/personagem_router.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import Personagem

router = APIRouter(
    prefix="/api/personagens",
    tags=["Personagens"]
)

@router.post("/", response_model=Personagem, status_code=status.HTTP_201_CREATED)
async def create_personagem(personagem: Personagem):
    await personagem.insert()
    return personagem

@router.get("/", response_model=List[Personagem])
async def get_all_personagens(skip: int = 0, limit: int = 10):
    personagens = await Personagem.find_all().skip(skip).limit(limit).to_list()
    return personagens

@router.get("/{nome_personagem}", response_model=Personagem)
async def get_personagem_by_name(nome_personagem: str):
    personagem = await Personagem.find_one(
        {"nome": {"$regex": f"^{nome_personagem}$", "$options": "i"}}
    )
    if not personagem:
        raise HTTPException(
            status_code=404,
            detail=f"Personagem '{nome_personagem}' não encontrado."
        )
    return personagem