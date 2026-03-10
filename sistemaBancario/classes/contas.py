from abc import ABC, abstractmethod
class Conta(ABC):
    def __init__(self, agencia : str, numero : str, saldo : float):
        self.agencia = agencia
        self.numero = numero
        self.saldo = float(saldo)
            
    def depositar(self, valor : float, cliente : Cliente, banco : Banco):
        if isinstance(valor, float) or isinstance(valor, int):
            if banco.autenticar(cliente, self):
                self.saldo += valor
            else:
                print("ERRO: Conta não autenticada!")
        else:
            print("ERRO: O valor passado para depósito deve ser um número [int | float]")

    @abstractmethod
    def sacar(self):
        ...
    
class ContaCorrente(Conta):
    def __init__(self, agencia : str, numero : str, saldo : float, extra : float):
        super().__init__(agencia, numero, saldo)
        self.extra = extra
    
    def sacar(self, valor : float, cliente : Cliente, banco : Banco):
        if isinstance(valor, float) or isinstance(valor, int):
            if banco.autenticar(cliente, self):
                if valor <= self.saldo + self.extra:
                    self.saldo -= valor
                else:
                    print("Saldo insuficiente")
            else:
                print("ERRO: Conta não autenticada!")
        else:
            print("ERRO: O valor passado para saque deve ser um número [int | float]")

class ContaPoupanca(Conta):
    def sacar(self, valor : float, cliente : Cliente, banco : Banco):
        if isinstance(valor, float) or isinstance(valor, int):
            if banco.autenticar(cliente, self):
                if valor <= self.saldo:
                    self.saldo -= valor
                else:
                    print("Saldo insuficiente")
            else:
                print("ERRO: Conta não autenticada!")
        else:
            print("ERRO: O valor passado para saque deve ser um número [int | float]")

if __name__ == "__main__":
    from cliente import Cliente
    from banco import Banco