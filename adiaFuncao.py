def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def criar_funcao(funcao, *args2):
    def executa(args1):
        return funcao(args1, *args2)
    return executa

cobaia = 10

# soma_com_cinco = lambda a: executa(soma,a, 5)
# multiplica_por_dez = lambda a: executa(multiplica,a, 10)
soma_com_cinco = criar_funcao(soma, 5)

print(soma_com_cinco(cobaia))
# print(multiplica_por_dez(cobaia))