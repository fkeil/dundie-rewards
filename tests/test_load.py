import os
import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

def setup_module():
    print()
    print("roda antes dos testes do modulo\n")

def teardown_module():
    print()
    print("roda apos os testes do modulo\n")

@pytest.fixture(scope="function") # , autouse=True para usar em todos os testes neste arquivo/modulo
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt") #cria novo arquivco
    file_.write("isso e sujeira...") #escreve no arquivo
    yield #libera para a execuvao da funcao, que vai rodar completamente
    file_.remove() #apos rodar as funcoes, remove o arquivo

@pytest.mark.unit
@pytest.mark.high
def test_load(request): # se colocar create_new_file dentro dos parenteses, apenas esta ffuncao vai usar as novas pastas de teste
    """"Test function load function"""
    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))
    
    with open(filepath, "w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'
