import numpy as np
import random
 
 
def meia (valor):
    if valor == 0:
        return 0
    elif valor == 1:
        return 12
    else:
        return 6
total = 0
matriz = np.zeros((10,15))
for i in range(10):
    for j in range(15):
        valor = random.randint(0,2)
        matriz[i,j] = valor
        total += meia(valor)
        
print(matriz)
print(total)