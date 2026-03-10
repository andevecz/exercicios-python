class Pessoa:
    def __init__(self, nome : str, idade : int):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome : str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade : int):
        self._idade = idade

class Cliente(Pessoa):
    def __init__(self, nome : str, idade : int, conta : ContaCorrente | ContaPoupanca = None):
        super().__init__(nome, idade)
        self.conta = conta
    
    def adicionar_conta(self, conta : ContaCorrente | ContaPoupanca):
        self.conta = conta

if __name__ == "__main__":
    from contas import ContaCorrente, ContaPoupanca