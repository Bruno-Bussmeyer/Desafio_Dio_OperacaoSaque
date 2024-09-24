#Variaveis
saldo = 500.45

opcao_menu = -1

#Menu
nome = (input("Inform seu nome: "))
print(f"Bem vindo {nome}! O que deseja fazer?")
opcao_menu = int(input("""
    ---------------Escolha uma opção---------------
      [0] - Consultar Saldo
      [1] - Saque
      [2] - Deposito
      [3] - Sair
"""))

#Ações de Usuario
while (opcao_menu != 3):

    if (opcao_menu == 0):
        print(f"O seu saldo é de: R$ {saldo} \n")

    if (opcao_menu == 1):
        valor_de_saque = float(input(f"O quanto você gostaria de sacar?: "))

        if (valor_de_saque > saldo):
            print("Você não tem saldo para esta operação!")

        if (valor_de_saque <= saldo):
            print(f"Você sacou R$ {valor_de_saque}!")
            saldo = saldo - valor_de_saque
            print(f"Seu saldo é de {saldo}")
        
    
    if (opcao_menu == 2):
        valor_de_deposito = float(input("Qual o valor do deposito?"))
        saldo = saldo + valor_de_deposito
        print(f"O seu saldo é de R$ {saldo}")

    opcao_menu = int(input("""
    Deseja realizar mais alguma operação?
      
          ---------------Escolha uma opção---------------
      [0] - Consultar Saldo
      [1] - Saque
      [2] - Deposito
      [3] - Sair
    """))

