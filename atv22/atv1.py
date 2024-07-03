import numpy as np
matriz = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        matriz[i,j] = int(input(f'Digite o número para a linha - {i+1} e para a coluna - {j+1} :'))
print(matriz)