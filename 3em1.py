import copy

from dados_3em1 import produtos

def trouxa_sort_dicts_in_lista(lista, parametro):
    i = 0
    j = 1
    tamanho = len(lista)
    while i < tamanho:
        while j < tamanho:
            if lista[i][parametro] < lista[j][parametro]:
                prodAux = lista[i]
                lista[i] = lista[j]
                lista[j] = prodAux
            j+=1
        j = 0
        i+=1
    return lista

novos_produtos = [
    {**p, "preco" : round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print(*novos_produtos, sep="\n")

#print(*novos_produtos, sep="\n")

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
trouxa_sort_dicts_in_lista(produtos_ordenados_por_nome, 'nome')

#print(*produtos_ordenados_por_nome, sep="\n")

produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_por_nome)
trouxa_sort_dicts_in_lista(produtos_ordenados_por_preco, 'preco')

#print(*produtos_ordenados_por_preco, sep="\n")

# outra maneira:

 # Lambda functions
produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda p : p['nome'])
produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda p : p['preco'])
print()
print(*produtos_ordenados_por_nome, sep="\n")
print()
print(*produtos_ordenados_por_preco, sep="\n")