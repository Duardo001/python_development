#importação do defaultdict
from collections import defaultdict
#criação de um default dict com uma lista como valor padrão
dicionario_lista = defaultdict(list)
dicionario_lista["PRODUTO"] = "Macbook Pro"
dicionario_lista["MARCA"] = "Apple"
print(f"Exibindo a chave PRODUTO do dicionario criado com uma lista: {dicionario_lista['PRODUTO']}")
print(f"Exibindo a chave PREÇO, que não existe no dicionario criado com uma lista: {dicionario_lista['PREÇO']}")
#Criação de função que retorna a frase "INEXISTENTE"
def funcao_exemplo():
    return "INEXISTENTE"
dicionario_funcao = defaultdict(funcao_exemplo)
dicionario_funcao["PRODUTO"] = "Macbook Pro"
dicionario_funcao["MARCA"] = "Apple"
print(f"\nExibindo a chave PRODUTO do dicionario criado com uma função: {dicionario_funcao['PRODUTO']}")
print(f"Exibindo a chave PREÇO, que não existe no dicionario criado com uma função: {dicionario_funcao['PREÇO']}")
#Criação de dicionário com uma função lambda
dicionario_lambda = defaultdict(lambda: "Não disponível")
dicionario_lambda["PRODUTO"] = "Macbook Pro"
dicionario_lambda["MARCA"] = "Apple"
print(f"\nExibindo a chave PRODUTO do dicionario criado com uma função lamda: {dicionario_lambda['PRODUTO']}")
print(f"Exibindo a chave PREÇO, que não existe no dicionario criado com uma função lambda: {dicionario_lambda['PREÇO']}")