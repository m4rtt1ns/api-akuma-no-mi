import google.generativeai as genai
import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
print("Carregando configurações...")
load_dotenv()

# Pega a chave da API do Google do ambiente
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "SUA_CHAVE_SECRETA_DA_API_DO_GOOGLE_AQUI":
    print("\nERRO: Chave da API do Google (GOOGLE_API_KEY) não encontrada ou não configurada no arquivo .env")
    exit()

# Configura a API do Gemini
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"\nERRO ao configurar a API do Google. Verifique se sua chave é válida. Detalhe: {e}")
    exit()


def buscar_sugestao_de_poder(nome_da_fruta: str):
    """Usa a IA do Google para buscar novas informações sobre uma fruta."""
    
    prompt = f"""
    Como um especialista em One Piece, pesquise e descreva de forma concisa 
    quaisquer novas habilidades, técnicas ou o status do Despertar para a Akuma no Mi 
    chamada '{nome_da_fruta}' que foram revelados recentemente no mangá de One Piece.
    
    Responda APENAS com as informações, de forma clara e direta. 
    Se não houver novidades significativas recentes, responda 'Nenhuma novidade encontrada.'.
    """
    
    try:
        print(f"Buscando atualizações para '{nome_da_fruta}'...")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Erro ao contatar a API do Gemini: {e}"

def main():
    """Função principal para rodar o script."""
    
    # URL da nossa API que já deve estar rodando
    api_url = "http://127.0.0.1:8000/api/akumanomi"
    
    print(f"Buscando lista de frutas da sua API em {api_url}...")
    
    try:
        # Pega a lista de todas as frutas da nossa API
        response = requests.get(api_url)
        response.raise_for_status()  # Isso vai gerar um erro se a API não responder com sucesso (ex: 404, 500)
        todas_as_frutas = response.json()
    except requests.exceptions.RequestException as e:
        print(f"\nERRO CRÍTICO: Não foi possível conectar à sua API em {api_url}.")
        print("Certifique-se de que o servidor (uvicorn) está rodando em outro terminal antes de executar este script.")
        print(f"Detalhe do erro: {e}")
        return  # Encerra o script

    if not todas_as_frutas:
        print("Nenhuma fruta encontrada na sua API. Adicione algumas frutas primeiro usando o /docs.")
        return

    print(f"Encontradas {len(todas_as_frutas)} frutas. Iniciando verificação de poderes...")
    
    for fruta in todas_as_frutas:
        nome = fruta['nome_romanizado']
        sugestao = buscar_sugestao_de_poder(nome)
        
        print("\n" + "="*50)
        print(f">>> Sugestão da IA para '{nome}':")
        print(sugestao)
        print("="*50)

# Isso faz com que a função main() seja executada quando você roda o arquivo
if __name__ == "__main__":
    main()