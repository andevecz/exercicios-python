while True:
    try:
        numero1 = float(input("Digite o primeiro número:\n"))
        numero2 = float(input("Digite o segundo número:\n"))
        operador = input("Digite o operador da conta:\n")
        resultado = -1

        match operador:
            case "+":
                resultado = numero1 + numero2
            case "-":
                resultado = numero1 - numero2
            case "*":
                resultado = numero1 * numero2
            case "/":
                resultado = numero1 / numero2
            case _:
                print("O operador escolhido é inválido!")
                continue

        print(f"O resultado da conta é: {resultado}")
        break
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
    except ValueError:
        print("Os valores digitados devem ser apenas números!")
    except:
        print("Algo deu errado!")