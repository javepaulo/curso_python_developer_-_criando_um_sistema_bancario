menu = """

O que deseja fazer?

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Digite uma das opções acima:  

"""


saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    # --------------------- Opção de depósito ------------------------

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\nValor inválido. Considere somente valor positivo.\n")

    # ----------------------------------------------------------------

    # ---------------------Opção de Saque ----------------------------

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("\nOperação não realizada. Saldo insuficiente.\n")
        
        elif excedeu_limite:
            print("\nOperação não realizada. Valor máximo por saque: R$500,00. Informe outro valor.\n")
        
        elif excedeu_saques:
            print("\nOperação não realizada. Sua conta tem um limite diário de 3 saques. Aguarde outro dia para realizar um novo saque.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        
        else:
            print("\nOperação não realizada. Considere somente valor positivo.\n")


    # ----------------------------------------------------------------

    # --------------------- Opção de Extrato -------------------------


    elif opcao == "3":
        print("\n============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")


    # ----------------------------------------------------------------

    # --------------------- Opção de Sair ----------------------------  


    elif opcao == "4":
        break


    # ----------------------------------------------------------------    

    else:
        print("\nOperação inválida, selecione apenas uma opção válida.\n")



