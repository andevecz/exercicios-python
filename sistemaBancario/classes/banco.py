class Banco:
    def __init__(self, contas = None):
        self.contas = contas or {}
    
    def criar_conta(self, nome : str, agencia : str, numero : str):
        self.contas[nome] = [agencia, numero]
    
    def autenticar(self, cliente : Cliente, conta : ContaCorrente | ContaPoupanca) -> bool:
        if cliente.nome in self.contas.keys():
            if [conta.agencia, conta.numero] in self.contas.values():
                print("Conta autenticada!")
                return True
            else:
                print("Conta não existe!")
        else:
            print("Cliente não existe!")
        
        return False

if __name__ == "__main__":
    from contas import ContaCorrente, ContaPoupanca
    from cliente import Cliente