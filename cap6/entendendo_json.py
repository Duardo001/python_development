#primeiro precisamos importar o módulo json
import json
#vamos criar um dicionário como exemplo
dicionario = {
    "nome":"Python",
    "missão":"Ser incrível!"
}
#Agora vamos utilizar a função dumps do módulo json para converter nosso dicionário
#O resultado será uma string com estrutura do JSON
texto = json.dumps(dicionario, indent=4, ensure_ascii=False)
print(f"O dicionário foi convertido para a str texto, e seu conteúdo é: {texto}")
#Já que o nosso JSON é só um texto, podemos gravá-lo normalmente
with open("arquivo.json", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto)
    print("Pronto! O texto no formato json foi salvo dentro de um arquivo!")