def sum_lists(list1,list2):
    return [x + y for x, y in zip(list1,list2)]

lista_a = [1,2,3,4]
lista_b = [3,4,5]

print(sum_lists(lista_a,lista_b))