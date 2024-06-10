# 3) Escreva um algoritmo que leia o valor de um vendedor, o salário fixo e o total de vendas efetuadas por ele no mês
#(em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas e salário no final do
#mês.

sF = float(input("salário fixo: "))
tV = float(input("total de vendas mês: "))

comissao = (tV/100) * 15
salario = comissao + sF

print("Seu salário é: R$", salario)



