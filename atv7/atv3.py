#Escreva um algoritmo que leia um vetor inteiro de 20 posições (vetor 1). Verifique os valores do vetor 1 e
#modifique um segundo vetor (vetor 2), atribuindo o valor “1” ao vetor 2 quando houver um valor nulo no primeiro vetor. Ao fim, imprima os dois vetores.
nulos = 0
vet = [1, 2, None, 4, None, None, 7, 8, 9, 10, 11, 12, None, 14, 15, None, 17, 18, 19]
for i in range(len(vet)):
    if vet[i] is None:
        nulos += 1
        
vet2 = [0]*nulos
for i in range(nulos):
    vet2[i] = 1
    
print(vet)
print(vet2)
