import numpy as np
matriz = np.full((4, 3), '', dtype=object)

def tab (i):
    if i == 0:
        return "nome"
    elif i == 1:
        return "email"
    else: 
        return "telefone"

for j in range(4):
    for i in range(3):
        matriz[j,i] = (input(f'Digite o {tab(i)} do usuario {j + 1}: '))
print(matriz)