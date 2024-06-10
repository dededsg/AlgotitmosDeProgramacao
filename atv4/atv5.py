#5. Ler um número inteiro e escrever o valor da soma de todos os números digitados até o momento,
#até que seja digitado um número negativo.

soma = 0
while True:
    valor = int(input("Digite um número positivo ou um negativo para finalizar: "))
    if valor < 0:
        break
    soma += valor

print("A soma de todos os números digitados é:", soma)