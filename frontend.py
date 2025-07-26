import streamlit as st
import requests
import pandas as pd

# URL da nossa API FastAPI (verifique se está correta)
API_URL = "http://127.0.0.1:8000/api/akumanomi/"

# Configuração da página para usar a largura total
st.set_page_config(layout="wide")

# --- FUNÇÃO PARA BUSCAR OS DADOS NA API ---
# O @st.cache_data é um "poder especial" do Streamlit.
# Ele guarda o resultado da função em cache. Ou seja, ele só vai
# chamar a API uma vez, e nas próximas vezes que a página recarregar,
# ele vai usar os dados guardados, deixando tudo super rápido.
@st.cache_data
def get_akuma_no_mi():
    """Busca todas as Akuma no Mi da nossa API."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []

# --- TÍTULO DA PÁGINA ---
st.title("🏴‍☠️ Grande Catálogo de Akuma no Mi 🍎")

# --- BUSCAR E EXIBIR OS DADOS ---
st.header("Frutas Cadastradas no Sistema")

frutas = get_akuma_no_mi()

if frutas:
    # Se a API retornou frutas, vamos mostrá-las

    # Convertendo os dados JSON para uma tabela com pandas
    df = pd.DataFrame(frutas)

    # Selecionando e renomeando apenas as colunas que queremos mostrar para ficar mais bonito
    df_display = df[['nome_br', 'tipo', 'descricao']]
    df_display = df_display.rename(columns={
        'nome_br': 'Nome',
        'tipo': 'Tipo',
        'descricao': 'Descrição'
    })

    # st.dataframe() exibe a tabela interativa na tela
    st.dataframe(df_display, use_container_width=True, hide_index=True)
else:
    # Se a API não retornou nada, mostramos uma mensagem de aviso
    st.warning("Nenhuma Akuma no Mi encontrada! Verifique se a API está rodando e se há dados cadastrados.")