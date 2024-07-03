import numpy as np

num_linhas = int(input("Digite o número de linhas"))
num_colunas = int(input("Digite o número de colunas"))

matriz = np.zeros((num_linhas,num_colunas))

for i in range(num_linhas):
    for j in range(num_colunas):
        matriz[i,j] = int(input(f'Digite o número para a linha - {i+1} e para a coluna - {j+1} :'))
print(matriz)