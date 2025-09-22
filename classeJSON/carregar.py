import json
from classes import Pessoa

CAMINHO_ARQUIVO = "exercícios/classeJSON/dados.json"

with open(CAMINHO_ARQUIVO, "r", encoding="utf8") as file:
    dicionario = json.load(file)

pessoa1 = Pessoa(**dicionario)

print(pessoa1.__dict__)
