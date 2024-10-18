#Função que calcula a velocidade média com base em dois parâmetros fornecidos, com dica sobre o tipo e um parâmetro opcional com valor padrão em km/h
def calcular_velocidade_media(distancia: float, tempo:float, unidade_medida="km/h"):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print(f"A velocidade média é {velocidade_media} {unidade_medida}")

#aqui começa o programa principal
#solicitar distância e tempo
dist_digitada = float(input("Digite a distância percorrida "))
tempo_dititado = float(input("Digite o tempo da viagem "))
#Ao chamar a função agora é necessário indicar valores para os parâmetros distancia e tempo
calcular_velocidade_media(dist_digitada, tempo_dititado)