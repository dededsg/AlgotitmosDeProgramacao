#Desafio! Desenvolva um algoritmo em Python capaz de abrir um arquivo de texto (*.txt)
#que contém o nome de todas cidades de Santa Catarina. Apresente cada linha do seu
#conteúdo em ordem alfabética. Pesquise recursos em Python que possam auxiliar na
#resolução dessa atividade. A apresentação deve seguir este formato, por ex.:
#“1. Araranguá | Num. De Hab.: 68.228 | Gentílico: araranguaense”


from os.path import realpath, dirname

caminho_arq = f'{dirname(realpath(__file__))}\\exemplo.txt'
with open(caminho_arq, "r", encoding="utf-8") as arquivo:
    
    for i,linha in enumerate(arquivo):
        i += 1
        print(i, linha)



