from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


"""

* from http import HTTPStatus *: Importação da biblioteca nativa do python que abstrai os códigos de resposta e nos 
apresenta o status.

* def test_root_deve_retornar_ok_e_ola_mundo() *: No nome da função, escrevemos geralmente o que o teste de fato faz. 
Aqui estamos dizendo que root deve retornar o status OK e a mensagem "olá mundo". Root é o nome dado a raiz da URL. 
O caminho /, que colocamos na definição do @app.get('/'). OK é o status que diz que a requisição aconteceu com 
sucesso no protocolo HTTP.

* client = TestClient(app) * Aqui criamos o cliente de teste do nosso app

* assert response.status_code == HTTPStatus.OK *: Aqui fazemos a validação do código de resposta, para saber se a 
resposta é referente ao código 200, que significa OK

* assert response.json() == {'message': 'Olá Mundo!'} *: No final, validamos se o dicionário que enviamos na função 
é o mesmo que recebemos quando fizemos a requisição.

"""