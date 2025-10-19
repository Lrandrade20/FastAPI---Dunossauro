import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# Estrutura fixture criado para linha de código 'TestClient(app)'
@pytest.fixture
def client():
    return TestClient(app)
