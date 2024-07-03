import numpy as np
import random
matriz = np.zeros((10,10))
for i in range(10):
    for j in range(10):
        matriz[i,j] = random.randint(0,10000)
print(matriz)