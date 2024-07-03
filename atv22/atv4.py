import numpy as np
import random
total = 0
matriz = np.zeros((4,6))
for i in range(4):
    for j in range(6):
        valor = int(input("Digite o total de moradores deste AP"))
        matriz[i,j] = valor
        total += valor
print(matriz)
print(total)
