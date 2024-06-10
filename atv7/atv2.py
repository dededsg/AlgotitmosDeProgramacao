#Escreva um algoritmo que leia um vetor de 15 elementos inteiros. Encontre e imprima na tela o menor elemento, assim como sua posição no vetor.

vet = [0]*15

for i in range(15):
    vet[i] = (input("Digite um valor inteiro: "))
menor = vet[i]   
for i in range(15):
    if vet[i] < menor:
        menor = vet[i]
        posicao = i

print("Número: " ,menor, "Posição do vetor: ",posicao)
    
    