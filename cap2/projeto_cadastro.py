print("\n--------------------------- Bem-vindo --------------------------")
print("------------------- Cadastro de doadores de sangue -------------------\n")
nome = input("Por favor, digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = int(input("Digite sua altura em centímetros: "))
idade = int(input("Digite sua idade: "))
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16
print("\n----------------------------------------------------------------")
print(f"\nFicha:\n\n\tNome: {nome.capitalize()}\n\tPeso: {peso}kg\n\tAltura: {altura}cm \n\tIdade: {idade} anos \n\tTem peso mínimo: {tem_peso_minimo}\n\tTem idade miníma: {tem_idade_minima}\n")
print("----------------------------------------------------------------\n")