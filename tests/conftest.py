import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# Criando essa variavel para evitar a repetição do client
# Codigo comentado nas duas primeiras funções
# para mostrar o exemplo de repetição
@pytest.fixture
def client():
    return TestClient(app)
