import json 
from pathlib import Path

data_dir = Path("data/raw")

for file_path in sorted(data_dir.glob("*.json")):
    with file_path.open("r", encoding="utf=8") as file:
        names = json.load(file)

    print(f"{file_path.name}: {len(names)} nomes")
