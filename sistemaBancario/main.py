from classes.contas import ContaCorrente, ContaPoupanca
from classes.banco import Banco
from classes.cliente import Cliente

santander = Banco()
santander.criar_conta("Aline", "001", "1000")

itau = Banco()
itau.criar_conta("André", "010", "1002")

print(f"CONTAS ITAU: {itau.contas}")
print(f"CONTAS SANTANDER: {santander.contas}")

aline = Cliente("Aline", 21)
aline.adicionar_conta(ContaCorrente("001", "1000", 10000, 2000))

andre = Cliente("André", 23)
andre.adicionar_conta(ContaPoupanca("010", "1002", 10000))

print(f"Saldo antigo de Aline: {aline.conta.saldo}")
aline.conta.sacar(11000, aline, santander)
print(f"Saldo após saque de Aline: {aline.conta.saldo}")
aline.conta.depositar(20000, aline, santander)
print(f"Saldo após depósito de Aline: {aline.conta.saldo}")

print("--------------------------------------")

print(f"Saldo antigo de André: {andre.conta.saldo}")
andre.conta.sacar(1000, andre, itau)
print(f"Saldo após saque de André: {andre.conta.saldo}")
andre.conta.sacar(9001, andre, itau)
andre.conta.depositar(20000, andre, itau)
print(f"Saldo após depósito de André: {andre.conta.saldo}")


