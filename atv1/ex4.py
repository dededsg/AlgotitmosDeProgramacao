#4) Leia dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o
#valor da variável B e a variável B passe a possuir o valor da variável A. Apresente os valores trocados.

a = float(input("Digite valor de A: "))
b = float(input("Digite valor de B: "))

c = a
a = b
b = c

print("Valor de A:", a)
print("Valor de B:", b)


