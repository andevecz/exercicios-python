import json
from classes import Pessoa

CAMINHO_ARQUIVO = "exercícios/classeJSON/dados.json"

pessoa1 = Pessoa("José", "Coutinho", 24, "São Paulo")

with open(CAMINHO_ARQUIVO, "w", encoding="utf8") as file:
    json.dump(pessoa1.__dict__, file, indent=2, ensure_ascii=False)
