import numpy as np
import random
total = 0
matriz = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        matriz[i,j] = int(input("Digite um valor"))
print(matriz)
valor = int(input("Digite um valor para multiplicar a matriz"))
print(matriz * valor)
print(total)