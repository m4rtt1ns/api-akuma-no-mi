# app/routers/akuma_no_mi_router.py
from fastapi import APIRouter, HTTPException, status
from typing import List

# CORREÇÃO IMPORTANTE AQUI:
# Usamos "app.models" para dizer ao Python para olhar dentro do nosso pacote "app".
from app.models import AkumaNoMi, NiveisPoder

# Cria um "roteador". Todos os endpoints aqui começarão com /api/akumanomi
router = APIRouter(
    prefix="/api/akumanomi",
    tags=["Akuma no Mi"]
)

@router.get("/", response_model=List[AkumaNoMi])
async def get_all_frutas():
    """Retorna uma lista de todas as Akuma no Mi cadastradas."""
    return await AkumaNoMi.find_all().to_list()

@router.get("/{nome_romanizado}", response_model=AkumaNoMi)
async def get_fruta_by_name(nome_romanizado: str):
    """Busca uma Akuma no Mi pelo seu nome romanizado."""
    fruta = await AkumaNoMi.find_one(AkumaNoMi.nome_romanizado == nome_romanizado)
    if not fruta:
        raise HTTPException(status_code=404, detail=f"Fruta '{nome_romanizado}' não encontrada.")
    return fruta

@router.post("/", response_model=AkumaNoMi, status_code=status.HTTP_201_CREATED)
async def create_fruta(fruta: AkumaNoMi):
    """Cria uma nova Akuma no Mi no banco de dados."""
    await fruta.insert()
    return fruta

@router.put("/{nome_romanizado}", response_model=AkumaNoMi)
async def update_poderes_fruta(nome_romanizado: str, niveis_poder_update: NiveisPoder):
    """Atualiza os níveis de poder de uma Akuma no Mi existente."""
    fruta = await AkumaNoMi.find_one(AkumaNoMi.nome_romanizado == nome_romanizado)
    if not fruta:
        raise HTTPException(status_code=404, detail=f"Fruta '{nome_romanizado}' não encontrada.")
    
    # Atualiza apenas o campo de poderes e salva a mudança no banco
    fruta.niveis_de_poder = niveis_poder_update
    await fruta.save()
    return fruta