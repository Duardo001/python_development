cavaleiros_jedi = ["Obi-Wan Kenobi", "Mace Windu", "Mestre Yoda", "Luke Skywalker", "Anakin Skywalker"]
print(f"A lista original é \n{cavaleiros_jedi}")
cavaleiros_jedi.append("Mestre Yoda")
print(f"Após a adição do elemento Mestre Yoda utilizando o append, a lista é \n{cavaleiros_jedi}")
print(f"O índice do elemento Mace Windu é {cavaleiros_jedi.index('Mace Windu')}")
cavaleiros_jedi.insert(1, "Rey")
print(f"Após a adição do elemento Rey na posição 1 utilizando o insert, a lista é \n{cavaleiros_jedi}")
print(f"A contagem do elemento Mestre Yoda é {cavaleiros_jedi.count('Mestre Yoda')}")
cavaleiros_jedi.pop()
print(f"Após o uso do pop, a lista é \n{cavaleiros_jedi}")
cavaleiros_jedi.pop(0)
print(f"Após o uso do pop com o índice 0, a lista é \n{cavaleiros_jedi}")
cavaleiros_jedi.reverse()
print(f"Após o uso do reverse, a lista é \n{cavaleiros_jedi}")
cavaleiros_jedi.sort()
print(f"Após o uso do sort, a lista é \n{cavaleiros_jedi}")
cavaleiros_jedi.sort()
print(f"Após o uso do sort(reverse=True), a lista é \n{cavaleiros_jedi}")