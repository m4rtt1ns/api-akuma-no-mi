# O Grande Catálogo das Akuma no Mi 🍎🏴‍☠️

Olá, Pirata! Este repositório é o nosso Log Pose para a jornada mais ambiciosa da Grand Line: catalogar todas as Akuma no Mi conhecidas pelo homem. Uma API forjada com o poder do Python e a velocidade do FastAPI, pronta para desvendar os maiores segredos do mundo.

O sonho de todo estudioso de Ohara, agora ao alcance de um clique!

## O que este Poneglyph Revela (Funcionalidades) ✨

* **📜 API Backend:**
    * Listagem, busca, cadastro e atualização de Akuma no Mi e Personagens.
    * Filtros avançados por tipo e usuário.
    * Sistema de paginação.
    * Relacionamento de dados entre Frutas e seus usuários.
* **👁️ Interface Frontend:**
    * Visualização interativa de todas as Akuma no Mi cadastradas.

## As Armas Secretas do Nosso Navio (Tecnologias) ⚙️

* **Backend:** Python, FastAPI, Beanie ODM, MongoDB
* **Frontend:** Streamlit, Pandas
* **Testes:** Pytest, Pytest-Asyncio, HTTPX
* **Servidor:** Uvicorn

## Como Içar Velas (Como Rodar o Projeto) 🗺️

Este projeto agora tem duas partes: a API (backend) e a Interface Visual (frontend). Você precisará de **dois terminais** para rodar tudo.

**1. Preparação Inicial**
   * Clone o repositório: `git clone ...`
   * Crie e ative o ambiente virtual: `python -m venv venv` e `.\venv\Scripts\activate`
   * Instale a tripulação (dependências): `pip install -r requirements.txt`

**2. Decifre o Poneglyph (`.env`)**
   * Crie o arquivo `.env` na raiz do projeto e adicione suas chaves do MongoDB Atlas e do Google AI.

**3. Ligar a API (Terminal 1)**
   ```bash
   # Com o ambiente virtual ativado
   uvicorn app.main:app --reload
   ```
   * *Sua API estará disponível em `http://127.0.0.1:8000`*

**4. Ligar o Frontend (Terminal 2)**
   ```bash
   # Abra um segundo terminal e ative o ambiente virtual
   streamlit run frontend.py
   ```
   * *Sua interface visual abrirá no seu navegador em `http://localhost:8501`*

---

Que seus sonhos sejam tão grandes quanto o One Piece!

-- *Capitão William Martins*
