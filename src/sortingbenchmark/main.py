
import json
from pathlib import Path

from sortingbenchmark.benchmarking.benchmark import executar_benchmark


# Caminho da pasta que contém os conjuntos de dados
DATA_DIR = Path(__file__).resolve().parents[3] / "dados"


# Arquivos que serão utilizados nos experimentos
arquivos = [
    "nomes_100000.json",
    "nomes_250000.json",
    "nomes_500000.json"
]


# Número de repetições de cada experimento
REPETICOES = 10


# Executar o benchmark para cada conjunto de dados
for nome_arquivo in arquivos:

    caminho = DATA_DIR / nome_arquivo

    with open(caminho, "r", encoding="utf-8") as file:
        lista = json.load(file)

    print(f"\nIniciando benchmark: {nome_arquivo}")
    print(f"Quantidade de nomes: {len(lista)}")

    executar_benchmark(lista, repeticoes=REPETICOES)


print("\nTodos os benchmarks foram concluídos!")
