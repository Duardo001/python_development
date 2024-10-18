#importação do OrderedDict
from collections import OrderedDict
dicionario_ordenado = OrderedDict()
print(f"O dicionario foi criado e ainda não contém nenhum valor: \n{OrderedDict}. Adicionaremos os seguintes valores e chaves: Nome:Iphone, Marca:Apple, Modelo:14 Pro Max")
#Adicionando chaves e valores
dicionario_ordenado["NOME"] = "Iphone"
dicionario_ordenado["MARCA"] = "Apple"
dicionario_ordenado["MODELO"] = "14 Pro Max"
print("\nPercorrendo o dicionario verificamos as seguintes chaves e valores: ")
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} --- {valor}")
dicionario_ordenado["MARCA"] = "Maçã"
print("\nAo alterar o valor da chave MARCA, percebemos que a ordem se mantém ")
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} --- {valor}")
dicionario_ordenado.pop("MARCA")
print("\nAo removermos a chave MARCA e percorrermos o dicionario, obtemos: ")
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} --- {valor}")
dicionario_ordenado["MARCA"] = "Apple"
print("\nAo reinserir a chave MARCA, notamos que passou a ser colocada na última posição ")
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} --- {valor}")