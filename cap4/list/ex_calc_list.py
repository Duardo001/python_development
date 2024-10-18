calorias = [];
resposta = ''

while resposta.upper() != "NÃO":
    caloria = int(input("\nPor favor, informe a quantidade de calorias consumidas nessa refeição:\n"))
    calorias.append(caloria)
    resposta = input("Deseja adicionar mais alguma refeição?\n- SIM\n- NÃO\n")
total = 0
print("\nCalorias ingeridas no dia:")
for caloria in calorias:
    total = total + caloria
    print(caloria)
media = total/len(calorias)
print(f"\nAo longo do dia foram consumidas {total} calorias, com uma média de {media:.2f} por refeição\n")