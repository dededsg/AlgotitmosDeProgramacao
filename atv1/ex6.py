#6) Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês.
#Considere fixo o juro da poupança em 0,70% a. m.

valor = float(input("Valor: "))
x = ((valor/100) * 0.70) + valor
print("seu valor com juros de um mês:" , x)