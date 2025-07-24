# O Grande Catálogo das Akuma no Mi 🍎🏴‍☠️

Olá, Pirata! Este repositório é o nosso Log Pose para a jornada mais ambiciosa da Grand Line: catalogar todas as Akuma no Mi conhecidas pelo homem. Uma API forjada com o poder do Python e a velocidade do FastAPI, pronta para desvendar os maiores segredos do mundo.

O sonho de todo estudioso de Ohara, agora ao alcance de um clique!

## O que este Poneglyph Revela (Funcionalidades) ✨

* **📜 Listar todas as Akuma no Mi conhecidas:** De Logias lendárias a Zoans míticas.
* **🔍 Buscar os segredos de uma fruta específica:** Descubra seus usuários e poderes ocultos.
* **✍️ Registrar uma nova fruta descoberta em suas viagens:** Contribua para o grande livro do conhecimento.
* **💥 Atualizar os poderes e o "Despertar" de uma fruta:** O poder não tem limites, e nossa API também não!

## As Armas Secretas do Nosso Navio (Tecnologias) ⚙️

* **Python 3.11+:** A linguagem antiga que nos permite ler os Poneglyphs.
* **FastAPI:** A velocidade de um *Gomu Gomu no Jet Pistol* para entregar os dados.
* **Beanie ODM & MongoDB Atlas:** O Baú do Tesouro infinito e seguro na nuvem para guardar todas as nossas frutas.
* **Uvicorn:** O vento em nossas velas que impulsiona o navio-servidor.

## O Mapa do Tesouro para a Execução 🗺️

Para iniciar sua própria jornada e usar esta API, siga o mapa:

**1. Encontre o Mapa (`git clone`)**
   ```bash
   git clone [https://github.com/SEU_USUARIO/api-akuma-no-mi.git](https://github.com/SEU_USUARIO/api-akuma-no-mi.git)
   cd api-akuma-no-mi
   ```

**2. Prepare seu Navio (Ambiente Virtual)**
   ```bash
   python -m venv venv
   # No Windows
   .\venv\Scripts\activate
   # No macOS/Linux
   source venv/bin/activate
   ```

**3. Reúna sua Tripulação (Instalar Dependências)**
   ```bash
   pip install -r requirements.txt
   ```

**4. Decifre o Poneglyph (Arquivo `.env`)**
   - Crie um arquivo `.env` na pasta principal.
   - Adicione suas chaves secretas, que são o verdadeiro tesouro:
     ```ini
     MONGO_DATABASE_URL="sua_string_de_conexao_do_atlas"
     DATABASE_NAME="akuma_db"
     GOOGLE_API_KEY="sua_chave_do_google_ai"
     ```

**5. Içar Velas! (Ligar o Servidor)**
   ```bash
   uvicorn app.main:app --reload
   ```

**6. Consulte seu Log Pose (Documentação)**
   - Com o navio navegando, aponte sua bússola para `http://127.0.0.1:8000/docs` para ver todas as rotas e testar os poderes da API.

## Próximos Destinos no Novo Mundo (Futuras Features) 🌊

* Adicionar imagens de todas as frutas.
* Criar um sistema de busca por usuário para encontrar todos os seus poderes.
* Implementar o script do Gemini para buscar informações automaticamente, como um Den Den Mushi superinteligente!

---

Que seus sonhos sejam tão grandes quanto o One Piece!

-- *Capitão William Martins*
