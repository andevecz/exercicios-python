class Motor:
    def __init__(self, nome):
        self._nome = nome

class Fabricante:
    def __init__(self, nome):
        self._nome = nome
        self._carros = []
    
    def fazer_carro(self, modelo, motor):
        self._carros.append(Carro(modelo, motor))

    def listar_carros(self):
        for carro in self._carros:
            print(f"O carro {carro._modelo} da fabricante {self._nome} tem o motor {carro._motor._nome}")

class Carro:
    def __init__(self, modelo, motor):
        self._modelo = modelo
        self._motor = motor

motor1 = Motor("V8")
motor2 = Motor("4x4")

fabricante1 = Fabricante("Toyota")
fabricante2 = Fabricante("Ford")
fabricante3 = Fabricante("Mitsubishi")

fabricante3.fazer_carro("ASX", motor1)
fabricante3.fazer_carro("Outlander", motor2)

fabricante3.listar_carros()