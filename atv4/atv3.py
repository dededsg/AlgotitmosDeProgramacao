#3. Crie um programa que lê dois números inteiros e imprime todos os números pares entre eles.
#Assuma que o segundo número é maior que o primeiro.


valor1 = int(input("digite um valor: "))
valor2 = int(input("digite um valor maior que o anterior: "))
valor1 += 1
for i in range(valor1, valor2):
    if i % 2 == 0:
        print(i)
