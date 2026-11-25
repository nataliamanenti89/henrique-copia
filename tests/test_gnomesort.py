
from sortingbenchmark.algorithms.gnomesort import gnome_sort


def test_lista_vazia():
    assert gnome_sort([]) == []


def test_lista_com_um_elemento():
    assert gnome_sort(["Ana"]) == ["Ana"]


def test_lista_desordenada():
    nomes = ["Igor", "Cecilia", "Evelyn", "Gustavo"]
    resultado = gnome_sort(nomes.copy())

    assert resultado == sorted(nomes)


def test_lista_em_ordem_inversa():
    nomes = ["Maria", "Joao", "Ana"]
    resultado = gnome_sort(nomes.copy())

    assert resultado == sorted(nomes)


def test_lista_com_nomes_repetidos():
    nomes = ["Ana", "Joao", "Ana", "Carlos"]
    resultado = gnome_sort(nomes.copy())

    assert resultado == sorted(nomes)
