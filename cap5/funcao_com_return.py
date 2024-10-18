def soma(a, b):
    resultado = a + b
    return resultado
valor1 = int(input("Informe o primeiro valor que deseja somar "))
valor2 = int(input("Informe o segundo valor que deseja somar "))
resposta = soma(valor1, valor2)
print(f"A variável resposta recebeu o return da função soma() e agora contém: {resposta}")
print(f"A função soma() está sendo chamada dentro deste print para os valores 10 e 15 e retornou: {soma(10, 15)}")