# app/routers/akuma_no_mi_router.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import AkumaNoMi, Personagem, AkumaNoMiRead, AkumaNoMiCreate, NiveisPoder

router = APIRouter(
    prefix="/api/akumanomi",
    tags=["Akuma no Mi"]
)

@router.get("/", response_model=List[AkumaNoMiRead])
async def get_all_frutas(skip: int = 0, limit: int = 10):
    frutas = await AkumaNoMi.find_all(fetch_links=True).skip(skip).limit(limit).to_list()
    return frutas

@router.post("/", response_model=AkumaNoMi, status_code=status.HTTP_201_CREATED)
async def create_fruta(fruta_data: AkumaNoMiCreate):
    akuma_no_mi_documento = AkumaNoMi(**fruta_data.model_dump())
    await akuma_no_mi_documento.insert()
    return akuma_no_mi_documento

@router.get("/{nome_romanizado}", response_model=AkumaNoMiRead)
async def get_fruta_by_name(nome_romanizado: str):
    fruta = await AkumaNoMi.find_one(
        AkumaNoMi.nome_romanizado == nome_romanizado, 
        fetch_links=True
    )
    if not fruta:
        raise HTTPException(status_code=404, detail=f"Fruta '{nome_romanizado}' não encontrada.")
    return fruta

@router.put("/{nome_romanizado}", response_model=AkumaNoMi)
async def update_poderes_fruta(nome_romanizado: str, niveis_poder_update: NiveisPoder):
    fruta = await AkumaNoMi.find_one(AkumaNoMi.nome_romanizado == nome_romanizado)
    if not fruta:
        raise HTTPException(status_code=404, detail=f"Fruta '{nome_romanizado}' não encontrada.")
    fruta.niveis_de_poder = niveis_poder_update
    await fruta.save()
    return fruta

@router.get("/tipo/{tipo_fruta}", response_model=List[AkumaNoMiRead])
async def get_frutas_by_tipo(tipo_fruta: str):
    frutas_encontradas = await AkumaNoMi.find(
        {"tipo": {"$regex": f"^{tipo_fruta}$", "$options": "i"}},
        fetch_links=True
    ).to_list()
    if not frutas_encontradas:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma fruta do tipo '{tipo_fruta}' foi encontrada."
        )
    return frutas_encontradas

@router.get("/usuario/{nome_usuario}", response_model=List[AkumaNoMiRead])
async def get_frutas_by_usuario(nome_usuario: str):
    personagem = await Personagem.find_one({"nome": {"$regex": f"^{nome_usuario}$", "$options": "i"}})
    if not personagem:
        raise HTTPException(status_code=404, detail=f"Personagem '{nome_usuario}' não encontrado.")
    
    frutas_encontradas = await AkumaNoMi.find(
        AkumaNoMi.usuario_atual.id == personagem.id,
        fetch_links=True
    ).to_list()

    if not frutas_encontradas:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma fruta encontrada para o usuário '{nome_usuario}'."
        )
    return frutas_encontradas

@router.put(
    "/{nome_fruta}/associar-usuario/{nome_personagem}", 
    response_model=AkumaNoMiRead,
    tags=["Relacionamentos"]
)
async def associar_usuario_a_fruta(nome_fruta: str, nome_personagem: str):
    fruta = await AkumaNoMi.find_one({"nome_romanizado": {"$regex": f"^{nome_fruta}$", "$options": "i"}})
    if not fruta:
        raise HTTPException(status_code=404, detail=f"Akuma no Mi '{nome_fruta}' não encontrada.")

    personagem = await Personagem.find_one({"nome": {"$regex": f"^{nome_personagem}$", "$options": "i"}})
    if not personagem:
        raise HTTPException(status_code=404, detail=f"Personagem '{nome_personagem}' não encontrado.")

    fruta.usuario_atual = personagem
    await fruta.save()
    
    # Recarregar a fruta com fetch_links=True para retornar o objeto completo
    fruta_atualizada = await AkumaNoMi.get(fruta.id, fetch_links=True)
    return fruta_atualizada