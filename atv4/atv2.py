#2. Crie um programa para ler 5 idades, calcular a média entre as idades e informar a média ao
#usuário.
soma = 0

for i in range(1, 6, 1):
    print("Digite a",i,"ª idade")
    valor = float(input())
    soma = valor + soma
print("A sua media de idade é:", soma/5)

