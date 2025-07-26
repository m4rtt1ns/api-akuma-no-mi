# scripts/seed_db.py
import requests
import json
# 1. IMPORTAMOS A FERRAMENTA DE "TRADUÇÃO" DE URLS
from urllib.parse import quote

# URL base da nossa API que deve estar rodando
API_URL = "http://127.0.0.1:8000/api"

def main():
    print("Iniciando o processo de popular o banco de dados...")

    with open("seed_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    personagens = data["personagens"]
    akuma_no_mi = data["akuma_no_mi"]
    associacoes = data["associacoes"]

    # Cadastra os Personagens (sem alteração aqui)
    print("\n--- Cadastrando Personagens ---")
    for p in personagens:
        try:
            response = requests.post(f"{API_URL}/personagens/", json=p)
            response.raise_for_status()
            print(f"Sucesso ao cadastrar {p['nome']}!")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao cadastrar {p['nome']}. Talvez já exista. Detalhe: {e.response.json()}")

    # Cadastra as Akuma no Mi (sem alteração aqui)
    print("\n--- Cadastrando Akuma no Mi ---")
    for a in akuma_no_mi:
        try:
            payload = {
                "nome_romanizado": a.get("nome_romanizado"),
                "nome_br": a.get("nome_br"),
                "tipo": a.get("tipo"),
                "descricao": a.get("descricao"),
                "niveis_de_poder": a.get("niveis_de_poder", {})
            }
            response = requests.post(f"{API_URL}/akumanomi/", json=payload)
            response.raise_for_status()
            print(f"Sucesso ao cadastrar {a['nome_romanizado']}!")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao cadastrar {a['nome_romanizado']}. Talvez já exista. Detalhe: {e.response.json()}")
    
    # Faz as Associações (AQUI ESTÁ A CORREÇÃO)
    print("\n--- Realizando Associações ---")
    for asc in associacoes:
        personagem_original = asc["personagem"]
        fruta_original = asc["fruta"]
        
        # 2. Usamos quote() para "traduzir" os nomes para o formato de URL
        # Ex: "Monkey D. Luffy" vira "Monkey%20D.%20Luffy"
        personagem_url = quote(personagem_original)
        fruta_url = quote(fruta_original)
        
        try:
            # 3. Agora usamos as versões "traduzidas" para montar a URL
            url = f"{API_URL}/akumanomi/{fruta_url}/associar-usuario/{personagem_url}"
            response = requests.put(url)
            response.raise_for_status()
            print(f"Sucesso ao associar '{fruta_original}' com '{personagem_original}'!")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao associar '{fruta_original}' com '{personagem_original}'. Detalhe: {e.response.json()}")
    
    print("\nProcesso de 'seed' finalizado!")

if __name__ == "__main__":
    main()