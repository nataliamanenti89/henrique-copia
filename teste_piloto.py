
import json
import random

from pathlib import Path
from sortingbenchmark.benchmarking.benchmark import executar_benchmark


# Carregar o conjunto de dados de 100 mil nomes
DATA_DIR = Path("dados")

with open(DATA_DIR / "nomes_100000.json", "r", encoding="utf-8") as file:
    lista_original = json.load(file)


# Selecionar 1.000 nomes para o teste-piloto
random.seed(23)
lista_teste = random.sample(lista_original, 1_000)


# Executar uma repetição do benchmark
executar_benchmark(
    lista_teste,
    repeticoes=1,
    nome_arquivo="benchmark_piloto.csv"
)
