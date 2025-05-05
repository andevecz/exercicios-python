import os
import time

perguntasERespostas = [
    {'Pergunta':'Quanto é 2+2?',
    'Opcoes' : ['1','2','3','4'],
    'Resposta': '4'},

    {'Pergunta':'Quanto é 9x2?',
    'Opcoes' : ['18','9','3','6'],
    'Resposta': '18'},
    
    {'Pergunta':'Quem foi Pedro Álvares Cabral?',
    'Opcoes' : ['O maior jogador de futebol da história.',
                'O homem que descobriu o Brasil.',
                'Cantor famoso.',
                'Criador do brigadeiro de colher.'],
    'Resposta': 'O homem que descobriu o Brasil.'},
]

while True:
    numeroPergunta = 0
    acertos = 0

    os.system("cls")
    print("Vai começar o show do milhão!!!\n")
    while numeroPergunta < len(perguntasERespostas):
        print(f"Pergunta número {numeroPergunta+1}:\n")
        print(perguntasERespostas[numeroPergunta]['Pergunta'])
        print(f"A. {perguntasERespostas[numeroPergunta]['Opcoes'][0]}\n"
              f"B. {perguntasERespostas[numeroPergunta]['Opcoes'][1]}\n"
              f"C. {perguntasERespostas[numeroPergunta]['Opcoes'][2]}\n"
              f"D. {perguntasERespostas[numeroPergunta]['Opcoes'][3]}\n")
        resposta = input("Reposta: ").upper()
        if resposta not in ['A','B','C','D']:
            print("Resposta inválida!")
            time.sleep(2)
            os.system("cls")
            continue
        match resposta:
            case 'A':
                if perguntasERespostas[numeroPergunta]['Opcoes'][0] == perguntasERespostas[numeroPergunta]['Resposta']:
                    print("Certa resposta!\n")
                    acertos+=1
                else:
                    print("Errou!\n")
            case 'B':
                if perguntasERespostas[numeroPergunta]['Opcoes'][1] == perguntasERespostas[numeroPergunta]['Resposta']:
                    print("Certa resposta!\n")
                    acertos+=1
                else:
                    print("Errou!\n")
            case 'C':
                if perguntasERespostas[numeroPergunta]['Opcoes'][2] == perguntasERespostas[numeroPergunta]['Resposta']:
                    print("Certa resposta!\n")
                    acertos+=1
                else:
                    print("Errou!\n")
            case 'D':
                if perguntasERespostas[numeroPergunta]['Opcoes'][3] == perguntasERespostas[numeroPergunta]['Resposta']:
                    print("Certa resposta!\n")
                    acertos+=1
                else:
                    print("Errou!\n")
        time.sleep(2)
        os.system("cls")
            
        numeroPergunta+=1
    print(f"Você acertou {acertos} perguntas!\n")
    if acertos <= 1:
        print("Que pena, estude mais!")
    elif acertos == 2:
        print("Foi quase, não desista!")
    elif acertos == 3:
        print("Parabéns! Você acaba de se tornar um milionário!")

    sair = input("Deseja sair?\n[S]im / [N]ão\n").upper()
    if sair == 'S':
        print("\nObrigado por jogar!")
        break
    elif sair == 'N':
        continue
    else:
        print("\nErro, valor inválido. Saindo do sistema.")
        break
