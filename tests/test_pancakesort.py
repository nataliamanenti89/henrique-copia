
from sortingbenchmark.algorithms.pancakesort import pancake_sort


def test_lista_vazia():
    assert pancake_sort([]) == []


def test_lista_com_um_elemento():
    assert pancake_sort(["Ana"]) == ["Ana"]


def test_lista_desordenada():
    nomes = ["Igor", "Cecilia", "Evelyn", "Gustavo"]

    resultado = pancake_sort(nomes.copy())

    assert resultado == sorted(nomes)


def test_lista_em_ordem_inversa():
    nomes = ["Maria", "Joao", "Ana"]

    resultado = pancake_sort(nomes.copy())

    assert resultado == sorted(nomes)


def test_lista_com_nomes_repetidos():
    nomes = ["Ana", "Joao", "Ana", "Carlos"]

    resultado = pancake_sort(nomes.copy())

    assert resultado == sorted(nomes)


def test_lista_original_preservada():
    nomes = ["Maria", "Ana", "Joao"]
    copia_original = nomes.copy()

    pancake_sort(nomes)

    assert nomes == copia_original
