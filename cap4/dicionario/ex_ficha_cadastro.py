op = 0
ficha = {}
while op != 4:
    print("\nFICHA CADASTRAL")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informação da ficha")
    print("3 - Exibir a ficha completa ")
    print("4 - Sair")
    op = int(input("Informe a opção desejada: "))
    if op == 1:
        chave = input("\nO que você deseja inserir como dado?\n")
        valor = input("\nInforme o valor desse dado:\n")
        ficha.update({chave:valor})
    elif op == 2:
        print(f"\nOs campos disóníveis para consulta são: {ficha.keys()}")
        resposta = input("O que você quer retornar da ficha?\n")
        if resposta in ficha.keys():
            print(f"{resposta} -> {ficha.get(resposta)}")
        else:
            print("O campo informado não existe")
    elif op == 3:
        print("------------- Ficha Completa -------------")
        for chave, valor in ficha.items():
            print(f"{chave.upper()} -- {valor}")
    elif op == 4:
        print("\nSaindo do sistema\n")
        break
    else:
        print("\n >>>>>>>>>>>>>>>> Opção inválida, tente novamente")