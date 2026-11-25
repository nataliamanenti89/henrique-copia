
import csv
import time
from pathlib import Path

from sortingbenchmark.algorithms.gnomesort import gnome_sort
from sortingbenchmark.algorithms.tournamentsort import tournament_sort
from sortingbenchmark.algorithms.pancakesort import pancake_sort


def executar_benchmark(
    lista,
    repeticoes=10,
    nome_arquivo="benchmark_oficial.csv"
):
    resultados = []

    # Referência para verificar a ordenação
    lista_esperada = sorted(lista)

    # Algoritmos disponíveis
    algoritmos = {
        "Gnome Sort": gnome_sort,
        "Tournament Sort": tournament_sort,
        "Pancake Sort": pancake_sort
    }

    # Sequência alternada das dez repetições
    ordens = [
        ["Gnome Sort", "Tournament Sort", "Pancake Sort"],
        ["Tournament Sort", "Pancake Sort", "Gnome Sort"],
        ["Pancake Sort", "Gnome Sort", "Tournament Sort"],
        ["Gnome Sort", "Pancake Sort", "Tournament Sort"],
        ["Pancake Sort", "Tournament Sort", "Gnome Sort"],
        ["Tournament Sort", "Gnome Sort", "Pancake Sort"],
        ["Gnome Sort", "Tournament Sort", "Pancake Sort"],
        ["Tournament Sort", "Pancake Sort", "Gnome Sort"],
        ["Pancake Sort", "Gnome Sort", "Tournament Sort"],
        ["Gnome Sort", "Pancake Sort", "Tournament Sort"]
    ]

    # Executar os experimentos
    for repeticao in range(1, repeticoes + 1):

        ordem_atual = ordens[(repeticao - 1) % len(ordens)]

        for nome in ordem_atual:

            algoritmo = algoritmos[nome]
            dados = lista.copy()

            inicio = time.perf_counter()
            resultado = algoritmo(dados)
            fim = time.perf_counter()

            tempo_execucao = fim - inicio

            if resultado is None:
                resultado = dados

            if resultado != lista_esperada:
                raise ValueError(
                    f"{nome} não ordenou corretamente os dados."
                )

            resultados.append({
                "algoritmo": nome,
                "tamanho": len(lista),
                "repeticao": repeticao,
                "tempo_segundos": tempo_execucao
            })

    # Salvar os resultados
    pasta = Path("resultados/brutos")
    pasta.mkdir(parents=True, exist_ok=True)

    arquivo = pasta / nome_arquivo

    escrever_cabecalho = (
        not arquivo.exists() or arquivo.stat().st_size == 0
    )

    with open(arquivo, "a", newline="", encoding="utf-8") as csvfile:

        campos = [
            "algoritmo",
            "tamanho",
            "repeticao",
            "tempo_segundos"
        ]

        escritor = csv.DictWriter(
            csvfile,
            fieldnames=campos
        )

        if escrever_cabecalho:
            escritor.writeheader()

        escritor.writerows(resultados)

    print(f"Benchmark concluído! Resultados salvos em: {arquivo}")
#python -m sortingbenchmark.benchmarking.main 
#e renomeia os resultados pra anteriores pra ter so um resultados oficias 