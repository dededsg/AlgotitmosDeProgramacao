#7. Dado um número inteiro positivo, determine se ele é ou não um número primo OBS: Um número
#primo é aquele que só é divisível por 1 e por ele próprio. Ex.: 7 -> 7/7 = 1; 7/1 = 7

valor = int(input("digite um valor inteiro positivo: "))

j = valor - 1
txt = "é primo"
print(valor)
for i in range(2, j, 1):
    print(i, "/", valor,"=")
    print(valor/i)
    if valor % i == 0: 
        txt = "o valor não é primo"
        break
print(txt)
