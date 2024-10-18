# .values(), .keys(), .items()
'''dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "lançamento": 1977,
    "bilheteria": 775000000.00
}
print(f"O método .keys() retorna \n{dicionario.keys()}")
print("Se percorrermos a lista retornada com um loop for teremos: ")
for chave in dicionario.keys():
    print(chave)
print(f"\nO método .values() retorna \n{dicionario.values()}")
print("Se percorrermos a lista retornada com um loop for teremos: ")
for valor in dicionario.values():
    print(valor)
print(f"\nO método .items() retorna \n{dicionario.items()}")
print("Como foi retornada uma lista de tuplas e as tuplas podem ser desempacotadas, teremos: ")
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")'''

#.get(), .setdefault(),.copy()
'''dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "lançamento": 1977,
    "bilheteria": 775000000.00
}
print(f"O método .get() para a chave diretor retorna \n{dicionario.get('diretor')}")
print(f"O método .get() para a chave publico (que não existe) retorna \n{dicionario.get('publico')}")
print(f"\nO método .setdefault() para a chave diretor retorna \n{dicionario.setdefault('diretor')}")
dicionario.setdefault("publico")
print(f"O método .setdefault() para a chave publico (que não existe) cria a chave e coloca o valor None. Veja como ficou nosso dicionário depois de utilizar este método: \n{dicionario}")
dicionario.setdefault("custo", 11000000.0)
print(f"Caso utilizemos o método .setdefault() para a chave custo (que não existe) e também passarmos um valor como argumento, a chave será criada com este valor. Veja como ficou nosso dicionário depois de utilizar este método: \n{dicionario}")
print(f"\nO método .copy() retorna a seguinte cópia do dicionário que, se for alterada, não impacta no dicionário original: {dicionario.copy()}")'''

#.update(), .pop(), .popitem(), .clear()
'''dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "lançamento": 1977,
    "bilheteria": 775000000.00
}
dicionario.update({"custo": 50.0})
print(f"O método .update() com a chave custo (que não existia) e o valor 50.0 nos deixa com o seguinte dicionário \n{dicionario}")
dicionario.update({"custo": 11000000.0})
print(f"O método .update() com a chave custo (que já existe após a mudança anterior) e o valor 11000000.0 nos deixa com o seguinte dicionário \n{dicionario}")
dicionario.pop("diretor")
print(f"\nO método .pop() para a chave diretor nos deixa com o seguinte dicionário \n{dicionario}")
dicionario.popitem()
print(f"\nO método .popitem() nos deixa com o seguinte dicionário \n{dicionario}")
dicionario.clear()
print(f"\nO método .clear() nos deixa com o seguinte dicionário \n{dicionario}")'''

#.fromkeys()
'''notas = dict.fromkeys(("Matemática", "Física", "Química"))
print(f"O dicionário gerado com o método fromkeys para a tupla de chaves (Matemática, Física, Química) e sem valor foi: \n{notas}")
notas = dict.fromkeys(("Matemática", "Física", "Química"), [])
print(f"\nO dicionário gerado com o método fromkeys para a tupla de chaves (Matemática, Física, Química) e valor zero foi: \n{notas}")'''
