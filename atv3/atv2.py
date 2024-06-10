#2. Escrever um algoritmo que leia dois valores inteiros distintos e informe qual é o maior

v1 = int(input('digite um valor'))
v2 = int(input('digite um valor distinto ao anterior'))

if v1 > v2 : 
    print('o valor', v1 , 'é maior que o valor', v2)
else :
    print('o valor', v2 , 'é maior que o valor', v1)
