def duplicaTriplicaQuadruplica(what : str):
    def duplica(numero : int):
        return numero*2
    
    def triplica(numero : int):
        return numero*3
    
    def quadruplica(numero : int):
        return numero*4
    
    match what:
        case "Duplica":
            return duplica
        case "Triplica":
            return triplica
        case "Quadruplica":
            return quadruplica
        
duplica = duplicaTriplicaQuadruplica("Duplica")
triplica = duplicaTriplicaQuadruplica("Triplica")
quadruplica = duplicaTriplicaQuadruplica("Quadruplica")

numero = int(input("Digite um número:\n"))
print(f"Número duplicado = {duplica(numero)}")
print(f"Número triplicado = {triplica(numero)}")
print(f"Número quadruplicado = {quadruplica(numero)}")