#8. Faça a tabuada de multiplicação (1 a 10) de um número inteiro fornecido pelo usuário.

valor = int(input("Digite um valor a ser multiplicado: "))
for i in range(1, 11, 1):
    mult = i * valor
    print(i,"*", valor,"=", mult)
    
