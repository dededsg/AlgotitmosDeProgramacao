#9. Crie um programa que lê um número maior que zero e imprime o dobro de todos os números
#entre 0 e o número lido.

valor = int(input("Digite um valor amior que 0: "))

for i in range(1, valor, 1):
    print(i+i)