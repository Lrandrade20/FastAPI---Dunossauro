from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_ex1_captura_do_response_do_html():
    client = TestClient(app)  # Arrange

    response = client.get('/ex1')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert '<h1> Olá Mundo </h1>' in response.text
    # print(response.text) 
