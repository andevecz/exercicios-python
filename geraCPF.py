import random

def geradorCPF() -> str:
    def calculaDigitos(cpfParcionado : str) -> str:
        multiplicador = 10
        resultado = 0
        for digito in cpfParcionado:
            resultado += int(digito)*multiplicador
            multiplicador-=1
        resto = resultado % 11
        digitoVerificadorJ = str(0 if resto < 2 else 11 - resto)
        cpfParcionado += digitoVerificadorJ
        
        multiplicador = 11
        resultado = 0
        for digito in cpfParcionado:
            resultado += int(digito)*multiplicador
            multiplicador-=1
        resto = resultado % 11
        digitoVerificadorK = str(0 if resto < 2 else 11 - resto)
        cpf = cpfParcionado + digitoVerificadorK
        return cpf
    
    tamanho = 9
    cpf = ''
    for _ in range(tamanho):
        cpf += str(random.choice(range(tamanho)))
    cpf = calculaDigitos(cpf)
    return cpf

def formataCPF(cpf : str) -> str:
    index = 0
    cpfFormatado = ''

    while index <= 10:
        if not index % 3 and index != 0 and index != 9:
            cpfFormatado += '.'
        elif index == 9:
            cpfFormatado += '-'
        cpfFormatado += cpf[index]
        index+=1
    return cpfFormatado



cpf = geradorCPF()
cpfFormatado = formataCPF(cpf)
print(f'CPF gerado: {cpfFormatado}')