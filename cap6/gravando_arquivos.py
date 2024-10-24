#texto_para_gravar = "Este texto será gravado!"
#a linha abaixo cria um objeto que representará o nosso arquivo.
#Ele está sendo aberto no modo de escrita, usando a codificação UTF-8
#with open("novo_arquivo.txt", "w", encoding="utf-8") as arquivo:
    #A instrução write escreve um conteúdo dentro do arquivo
    #arquivo.write(texto_para_gravar)

#a linha abaixo cria um objeto que representará o nosso arquivo.
#Ele está sendo aberto no modo de leitura, usando a codificação UTF-8
with open("novo_arquivo.txt", "r", encoding="utf-8") as arquivo:
    #A instrução .read() lê o conteúdo em formato de string
    conteudo = arquivo.read()
#A linha abaixo exibe o conteúdo que foi lido
print(conteudo)