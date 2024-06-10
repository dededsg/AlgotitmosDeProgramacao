#Fazer um algoritmo que leia um vetor de 10 posições de números inteiros e mostre somente os positivos não-nulos
#(maiores que zero). Obs: o vetor não deve conter espaços (posições) vazios.


vet = [0]*10
for i in range(10):
    vet[i] = int(input("Digite um valor inteiro: "))

for i in range(10):
    if vet[i] > 0:
        print(vet[i])