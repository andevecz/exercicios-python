def zipper(lista1, lista2):
    tamanho1 = len(lista1)
    tamanho2 = len(lista2)
    escolhido = min(tamanho1,tamanho2)
    
    return [(lista1[i],lista2[i]) for i in range(escolhido)]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista1,lista2))

print(list(zip(lista1,lista2)))

# ou

lista3 = ['São João da Boa Vista', 'Feira de Santana', 'Poços de Caldas', 'Brusque']
lista4 = ['SP', 'BA', 'MG', 'SC', 'RJ']

print(list(zip(lista3,lista4)))