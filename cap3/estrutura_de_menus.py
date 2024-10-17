opcao = 0
while opcao != 3:
    print("\n-------------------------- Bem-Vindo--------------------------")
    print("\n1 - Receber um elogio")
    print("2 - Calcular o fatorial de um número")
    print("3 - Sair\n")
    opcao = int(input("Informe o número da opção desejada e depois tecle ENTER: "))
    if opcao == 1:
        #instruções para o caso de o usuário ter escolhido a opção 1
        print("\nVocê é uma pessoa legal!!")
    elif opcao == 2:
        #instruções para o caso de o usuário ter escolhido a opção 2
        numero = int(input("Digite o nº desejado\n"))
        for valor in range(1, numero, 1):
            numero = numero * valor
        print(f"\n>>>>>>>>>>>>>>>>>>>>>>> O fatorial de desse número é: {numero}")
    elif opcao == 3:
        #Instruções para o caso de o usuário ter escolhido a opção 3
        print("\nEncerrando programa...\n")
        break
    else:
        #Instruções para o caso de o usuário não ter escolhido nenhuma opção válida
        print("Nenhuma opção válida foi selecionada!! Tente novamente.")