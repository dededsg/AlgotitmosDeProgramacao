#Faça um programa em Python que receba uma lista com 10 valores inteiros e mostre para
#o usuário qual número é o maior e qual é o menor.
valorMax = float(input("Digite um valor"))
valorMin = valorMax
for i in range(1 , 10 , 1):
    valor = float(input("Digite um valor"))
    if valor > valorMax:
        valorMax = valor
    elif valor < valorMin:
        valorMin = valor
print (f'maior valor: {valorMax} menor valor: {valorMin}')
        
        