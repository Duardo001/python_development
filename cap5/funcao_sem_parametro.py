#Função que calcula a velocidade média
def calcular_velocidade_media():
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print(f"A velocidade média é {velocidade_media}")

#aqui começa o programa principal
#solicitar distância e tempo
distancia = float(input("Digite a distância percorrida "))
tempo = float(input("Digite o tempo da viagem "))
calcular_velocidade_media()