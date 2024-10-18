def calcular_velocidade_media (distancia: float, tempo:float, unidade_medida="km/h"):
    if tempo == 0:
        return 0
    velocidade_media = distancia/tempo
    return f"A velocidade média foi de {velocidade_media} {unidade_medida}"

def converte_temp(temperatura:float, unidade_medida="°C"):
    if unidade_medida.upper() == "C":
        return (temperatura * 1.8) + 32
    elif unidade_medida.upper() == "F":
        return (temperatura - 32) / 1.8      
    else:
        return 0

def exibir_menu():
    print("\n--------------------- MENU ---------------------")
    print("1 - Calcular velocidade média")
    print("2 - Converter temperatura")
    print("3 - Sair")
    
def aluno_fisica():
    op = 0
    while op != 3:
        exibir_menu()
        op = int(input("Digite a opção desejada: "))
        if op == 1:
            distancia = float(input("\nDistância percorrida: "))
            tempo = float(input("\nTempo: "))
            medida = input("\nInforme a medida (ms/s ou km/h): ")
            print(f"\n{calcular_velocidade_media(distancia, tempo, medida)}")
            
        elif op == 2:
            temperatura = float(input("\nInforme o valor da temperatura: "))
            medida = input("Informe o valor dessa medida (C ou F): ")
            print(f"\nO resultado da conversão é {converte_temp(temperatura, medida)}")
        elif op == 3:
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida!!")
