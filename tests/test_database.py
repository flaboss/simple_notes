import os
import pytest
from database import NoteManager

TEST_DB = "notes_test.json"


@pytest.fixture(autouse=True)
def setup_database():
    # Configura o NoteManager para usar o banco de teste
    NoteManager.set_storage(TEST_DB)

    # Limpa o arquivo de teste antes de começar
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    yield

    # Limpa após o teste para não deixar lixo na pasta
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_save_and_get_note():
    NoteManager.save("test title", "Test content")
    notas = NoteManager.get_all()
    assert len(notas) == 1


def test_delete_note():
    """Testa se a exclusão de uma nota funciona"""
    NoteManager.save("Nota para Deletar", "Texto")
    notas_antes = NoteManager.get_all()
    nota_id = notas_antes[0]["id"]

    NoteManager.delete(nota_id)

    notas_depois = NoteManager.get_all()
    assert len(notas_depois) == 0

def test_search_notes():
    """Testa a funcionalidade de busca de notas"""
    NoteManager.save("Primeira Nota", "Conteúdo da primeira nota")
    NoteManager.save("Segunda Nota", "Conteúdo da segunda nota")
    NoteManager.save("Outra Coisa", "Conteúdo diferente")

    results = NoteManager.search("Nota")
    assert len(results) == 2
    titles = [nota["title"] for nota in results]
    assert "Primeira Nota" in titles
    assert "Segunda Nota" in titles
