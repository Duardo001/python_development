# def exibe_saudacao(**cliente):
#     print(f"É muito bom ter você como cliente, {cliente['nome']} {cliente['sobrenome']}")
# exibe_saudacao(nome="André", sobrenome="David")

def exibe_ficha(**dados):
    print(dados)
    print("----FICHA----")
    for chave, valor in dados.items():
        print(f"{chave.upper()} -- {valor}")
ficha_cliente = {
    "nome":"Dino da Silva Sauro",
    "estado civil":"casado",
    "camisa":"xadrez",
    "filhos": True
}
exibe_ficha(**ficha_cliente)