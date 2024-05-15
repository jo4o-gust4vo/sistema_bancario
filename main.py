#variaveis


menu = '''
        \n ===================MENU===================

                [D] - DEPOSITO
                [S] - SAQUE
                [E] - EXTRATO
                [Q] - SAIR
>>'''

saque = 0
deposito = 0
extrato = ''
limite = 500
LIMITE_SAQUES = 3
contandador_saque = 1

while True:


    opcao = (input(menu))

    if opcao == 'D':
        valor_deposito = float(input('Valor a ser depositado: '))

        if valor_deposito > 0:
            deposito += valor_deposito
            extrato += f'Valor depositado: R$ {valor_deposito}\n'
        else:
            print('Operação inválida. Tente novamente.')

    elif opcao == 'S':

        valor_saque = float(input('Valor a ser saque: '))

        if valor_saque > limite:
            print('Operação invalida')
        elif valor_saque > deposito and deposito != 0:
            print('Operação invalida, pois o valor do saque é maior do que o valor em conta.')
        elif contandador_saque > LIMITE_SAQUES:
            print('Operação inválida. Foi excedido o limite de saque.')
        elif deposito == 0:
            print('Operação inválida, pois o saldo é 0.')
        elif valor_saque > 0:
            deposito -= valor_saque
            extrato += f'valor de saque: R$ {valor_saque}\n'
            contandador_saque += 1
        else:
            print('Operação invalida. Tente novamente.')
    elif opcao == 'E':
        print("\n================ EXTRATO ================")
        if extrato == '':
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"\nSaldo: R$ {deposito:.2f}")
            print("==========================================")


    elif opcao == 'Q':
        break

    else:
        print('Operação invalida. Tente novamente.')





