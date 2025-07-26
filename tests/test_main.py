from httpx import AsyncClient

# Nossos testes precisam ser 'async' porque a API é assíncrona.
# O 'test_client' é a nossa 'fixture' mágica do conftest.py.
# O Pytest vai automaticamente criá-lo e passá-lo para a nossa função.
async def test_read_root(test_client: AsyncClient):
    """
    Testa se o endpoint raiz ("/") está funcionando corretamente.
    """
    # 1. FAZER A CHAMADA:
    # Usamos o test_client para fazer uma requisição GET para a rota "/".
    response = await test_client.get("/")

    # 2. VERIFICAR A RESPOSTA:
    # A palavra 'assert' é a chave dos testes.
    # Ela verifica se uma condição é verdadeira. Se não for, o teste falha.

    # Verificamos se o código de status da resposta é 200 (OK, sucesso!)
    assert response.status_code == 200

    # Verificamos se o corpo da resposta (o JSON) é exatamente o que esperamos
    assert response.json() == {
        "message": "Bem-vindo à API de Akuma no Mi! Acesse /docs para ver a documentação."
    }