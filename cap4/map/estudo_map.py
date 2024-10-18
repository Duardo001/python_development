lista = ["Python", "Java", "Fortran", "Cobol", "C++"]
mapa = map(len, lista)
print(f"Criamos a seguinte lista: \n{lista}")
print(f"Se tentarmos exibir o mapa que foi gerado aplicando a função len à lista, teremos apenas seu endereço de memória: \n{mapa}")
lista_do_mapa = list(mapa)
print(f"Convertendo o mapa para o tipo list, obtemos o resultado da aplicação da função len a cada uma das palavras da lista original: \n {lista_do_mapa}")
print(f"\nApesar de termos criado objetos para armazenarem o mapa e a lista convertida, o mesmo efeito poderia ser atingido escrevendo em um print list(map(len, lista)): \n{list(map(len, lista))}")