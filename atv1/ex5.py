#5) Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar
#(U$$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o
#usuário.

dolar = float(input("Valor em doletas: "))
cot = float(input("Valor da cotação: "))

print("Vc tem: R$", (dolar * cot))