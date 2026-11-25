
import json
from faker import Faker
from pathlib import Path


# Configurações dos experimentos
SEED = 23
SIZES = [100_000, 250_000, 500_000]

# Pasta onde os conjuntos de dados serão salvos
DATA_DIR = Path("dados")
DATA_DIR.mkdir(parents=True, exist_ok=True)


# Gerar nomes fictícios
def generate_names(size):
    fake = Faker("pt_BR")
    fake.seed_instance(SEED + size)

    names = [fake.name() for _ in range(size)]

    return names


# Gerar e salvar os três conjuntos de dados
def main():
    for size in SIZES:

        print(f"Gerando conjunto com {size} nomes...")

        names = generate_names(size)

        output_file = DATA_DIR / f"nomes_{size}.json"

        with output_file.open("w", encoding="utf-8") as file:
            json.dump(names, file, ensure_ascii=False, indent=2)

        print(f"Arquivo salvo: {output_file}")


if __name__ == "__main__":
    main()
