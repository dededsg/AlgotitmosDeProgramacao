file = "exemplo.txt"

teste = open(file , 'r', encoding="utf-8")

for i,linha in enumerate(teste):
    i += 1
    print(i, linha)