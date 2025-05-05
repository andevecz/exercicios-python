def criar_multiplicador(multiplicador : int):
    def multiplicar(numero : int) -> int:
        return numero * multiplicador
    return multiplicar

NUMERO_TESTE = 2

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(f"Número duplicado : {duplicar(NUMERO_TESTE)}")
print(f"Número triplicado : {triplicar(NUMERO_TESTE)}")
print(f"Número quadruplicado : {quadruplicar(NUMERO_TESTE)}")

print(type(duplicar))