import time
import os
import json

def listar(lista : list):
    print("Sua lista contém os seguintes valores:\n")
    for item in lista:
        print(f"{item}")

def desfazer(lista : list, aux: list):
    if not lista:
        print("ERRO: Lista vazia")
    else:
        itemAux = lista.pop(-1)
        aux.append(itemAux)
        print(f"Item '{itemAux}' removido.")

def refazer(lista : list, aux: list):
    if not aux:
        print("Não existe valor a ser refeito.")
    else:
        itemAux = aux.pop(-1)
        lista.append(itemAux)
        print(f"Item '{itemAux} ' adicionado novamente na lista")

def sair_salvar(lista : list):
    with open("exercícios/listaTarefas/tarefas.json", "w", encoding="utf8") as file:
        json.dump(lista, file, indent=2, ensure_ascii=False)

try:
    with open("exercícios/listaTarefas/tarefas.json", "r", encoding="utf8") as file:
        lista = json.load(file)
except FileNotFoundError:
    lista = []
aux = []

while True:
    os.system("cls")
    print("Bem-vindo ao programa da Lista de Tarefas!\n",
          "Digite um item para adicionar à lista ou uma ação: [\"/ajuda\" para listar ações]")
    action = input(" ")

    if action[0] == "/":
        match action.upper():
            case "/AJUDA":
                print("Lista de ações:\n",
                      "/listar - Mostra os itens da lista\n",
                      "/desfazer - Remove o último item adicionado na lista\n",
                      "/refazer - Cancela a operação de desfazer\n",
                      "/sair - Sai do programa\n")
                input("\nPRESSIONE ENTER PARA CONTINUAR")
                
            case "/LISTAR":
                os.system("cls")
                listar(lista)
                input("\nPRESSIONE ENTER PARA CONTINUAR")

            case "/DESFAZER":
                desfazer(lista, aux)
                input("\nPRESSIONE ENTER PARA CONTINUAR")

            case "/REFAZER":
                refazer(lista, aux)
                input("\nPRESSIONE ENTER PARA CONTINUAR")

            case "/SAIR":
                sair_salvar(lista)
                print("\nTarefas salvas em um arquivo JSON!")
                print("\nObrigado por utillizar o software!")
                break

            case _:
                print("ERRO: A instrução passada não existe")
                time.sleep(2)
    else:
        lista.append(action)