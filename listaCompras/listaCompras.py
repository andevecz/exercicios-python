import os
import time

def inserir(lista : list):
    os.system("cls")
    insercao = input("O quê você gostaria de inserir na lista?\n")
    lista.append(insercao)

def apagar(lista : list) -> list:
    os.system("cls")
    for index, item in enumerate(lista):
        print(f"{index}. {item}")
    insercao = int(input("O quê você gostaria de apagar da lista? (Digite o índice do item)\n"))
    try:
        lista.pop(insercao)
    except:
        print("Erro. Este índice não existe!")
        time.sleep(2)
    return lista

def listar(lista: list) -> str:
    os.system("cls")
    listar = "Lista de compras:\n"
    for item in lista:
        listar += f"- {item}\n"
    return listar

listaCompras = []
print("** Seja bem-vindo à sua lista de compras! **\n")
while True:
    print("Selecione uma opção: \n"       \
          "A. Inserir um item na lista.\n"\
          "B. Remover um item da lista.\n"\
          "C. Listar os itens da lista.\n"\
          "D. Sair da lista de compras\n")
    selecao = input().upper()
    match selecao:
        case 'A':
            inserir(listaCompras)
            os.system("cls")
        case 'B':
            listaCompras = apagar(listaCompras)
            os.system("cls")
        case 'C':
            print(listar(listaCompras))
            input("\nPressione ENTER para continuar.")
            os.system("cls")
        case 'D':
            os.system("cls")
            arquivo = open("Lista de Compras.txt", 'w')
            arquivo.write(listar(listaCompras))
            print("Obrigado por utilizar o programa!\n" \
                  "A sua lista de compras foi criada!")
            break