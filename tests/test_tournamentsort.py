
from sortingbenchmark.algorithms.tournamentsort import tournament_sort


def test_lista_vazia():
    assert tournament_sort([]) == []


def test_lista_com_um_elemento():
    assert tournament_sort(["Ana"]) == ["Ana"]


def test_lista_desordenada():
    nomes = ["Igor", "Cecilia", "Evelyn", "Gustavo"]

    resultado = tournament_sort(nomes)

    assert resultado == sorted(nomes)


def test_lista_em_ordem_inversa():
    nomes = ["Maria", "Joao", "Ana"]

    resultado = tournament_sort(nomes)

    assert resultado == sorted(nomes)


def test_lista_com_nomes_repetidos():
    nomes = ["Ana", "Joao", "Ana", "Carlos"]

    resultado = tournament_sort(nomes)

    assert resultado == sorted(nomes)


def test_lista_original_preservada():
    nomes = ["Maria", "Ana", "Joao"]
    copia_original = nomes.copy()

    tournament_sort(nomes)

    assert nomes == copia_original
