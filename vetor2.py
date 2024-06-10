n = 6
vet = [0]*n
negativo = 0
p = 0
j = 1
for i in range(6):
    valor = float(input("Digite um valor: "))
    vet[i] = valor
    if valor < 0:
        negativo += 1
        neg = [0]*n   
        neg[p] = valor
        print(p)
        p += 1
        

print(negativo)
print(vet)
print(neg)
