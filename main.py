import contas
import pessoas

conta = contas.ContaCorrente(111, 4444, 100, 0)
ana = pessoas.Cliente('Ana', 21, conta)
banco = contas.Banco()
banco.autenticar(ana, ana.to_list())
conta.sacar(100)
