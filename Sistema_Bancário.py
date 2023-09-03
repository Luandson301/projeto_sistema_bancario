menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

= '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcão  = input(menu)

    if opcão == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou, valor informado é invalido")
    
    elif opcão == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, saldo insuficiente")
        
        elif excedeu_limite:
            print("Operação falhou, valor excede o limite disponível")

        elif excedeu_saques:
            print("Operação falhou, numero de saques diarios excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou, valor informado é invalido")

    
    elif opcão == "e":
        print("\n---------------- EXTRATO --------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------------------")

    elif opcão == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada")
