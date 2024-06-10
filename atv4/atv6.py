#6. Ler 5 números inteiros informados pelo usuário, e ao final mostrar a soma desses números. a.
#Complementar o exercício 6 informando, ao final, se a soma representa um número par ou ímpar.

soma = 0
for i in range(1, 6, 1):
    print("Digite um valor a ser somado")
    valor = float(input())
    soma = valor + soma
if soma % 2 == 0:
    txt = "par"
else:
    txt = "ímpar"
print("A soma é:", soma, "o valor é", txt)

