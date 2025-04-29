import re

def validaCPF(cpf : str) -> bool:
    def validaFormatoCPF (cpf : str) -> bool:
        regexCPF = r'^\d{3}.\d{3}.\d{3}-[\dXY]{2}$'
        if re.match(regexCPF, cpf):
            return True
        else:
            return False
        
    def validaCalculoDigitoJ(cpf : str) -> bool:
        cpfParcionadoLista = cpf[:11].split('.')
        cpfParcionado = ''
        resultado = 0
        multiplicador = 10

        for partes in cpfParcionadoLista:
            cpfParcionado += partes

        for digito in cpfParcionado:
            resultado += int(digito)*multiplicador
            multiplicador-=1
        resto = resultado % 11
        digitoVerificador = str(0 if resto < 2 else 11 - resto)
        if digitoVerificador == cpf[12]:
            return True
        else:
            return False
        
    def validaCalculoDigitoK(cpf : str) -> bool:
        cpf = cpf.replace('-', '.')
        cpfParcionadoLista = cpf[:13].split('.')
        cpfParcionado = ''
        resultado = 0
        multiplicador = 11

        for partes in cpfParcionadoLista:
            cpfParcionado += partes
        for digito in cpfParcionado:
            resultado += int(digito)*multiplicador
            multiplicador-=1
        resto = resultado % 11
        digitoVerificador = str(0 if resto < 2 else 11 - resto)
        if digitoVerificador == cpf[13]:
            return True
        else:
            return False
    
    if validaFormatoCPF(cpf) and validaCalculoDigitoJ(cpf) and validaCalculoDigitoK(cpf):
        return True
    else:
        return False
    
def encontraEstado (cpf : str) -> str:
    if not validaCPF(cpf):
        return 'ERRO: CPF Inválido'
    else:
        dicionarioEstados = {'1': 'Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins',
                             '2': 'Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima',
                             '3': 'Ceará, Maranhão ou Piauí',
                             '4': 'Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas',
                             '5': 'Bahia ou Sergipe',
                             '6': 'Minas Gerais',
                             '7': 'Rio de Janeiro ou Espírito Santo',
                             '8': 'São Paulo',
                             '9': 'Paraná ou Santa Catarina',
                             '0': 'Rio Grande do Sul'}
        for digito in dicionarioEstados.keys():
            if cpf[10] == digito:
                return dicionarioEstados[digito]

# Exemplos de CPF para utilizar diretamente no código
CPF_CERTO = '123.456.789-09'
CPF_J_ERRADO = '123.456.789-19'
CPF_K_ERRADO = '123.456.789-08'
CPF_FORMATO_ERRADO = '123456.789-09'

cpf = input("Digite o CPF.\n")

if validaCPF(cpf):
    estados = encontraEstado(cpf)
    print("\nCPF válido.")
    print(f"Este CPF foi emitido em {estados}.")
else:
    print("\nCPF inválido.")

