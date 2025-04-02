import os

def plotResultado(resposta : str, tentativas : int):
    os.system("cls")
    print(f"Palavra secreta: {resposta}")
    print(f"Tentativas: {tentativas}\n")

palavraSecreta = "segredo"
tentativas = 0
i = 0
resposta = "*"

while i < len(palavraSecreta):
    letraDigitada = input("Digite uma letra:\n")
    if len(letraDigitada) == 1:
        if palavraSecreta[i] == letraDigitada:
            if resposta[-1] == '*':
                resposta = resposta.replace('*','')
            resposta += letraDigitada
            plotResultado(resposta, tentativas)
        else:
            if resposta[-1] != '*':
                resposta += '*'
            plotResultado(resposta, tentativas)
            continue
    else:
        print("Você deve escrever apenas UMA letra.")
        continue
    i+=1

print("Parabéns! Você adivinhou a palavra secreta!")