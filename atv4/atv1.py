#1. Crie um programa que lê um número inteiro, maior que 0, e imprime a soma entre todos os
#números menores que o número lido, até chegar em 0. Exemplo: usuário informa o numero 10 -> 9
#+ 8 + 7 + ... + 1
#ta aceitando menor que 0 tbm 

valor = int(input("Digite um valor:"))

if valor >= 0:
    a = -1
else:
    a = 1
result = 0

for i in range(valor, 0, a):
    result = result + i
print("o valor é: ", result - valor)