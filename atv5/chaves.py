#Faça um programa que imprima na tela a versão completa do verso do Chaves: “O Cão
#Arrependido”. O verso deve ser repetido 44 vezes.


from os.path import realpath, dirname
for j in range(1, 45, 1):
    print(f'vez: {j}')
    caminho_arq = f'{dirname(realpath(__file__))}\\chaves.txt'
    with open(caminho_arq, "r", encoding="utf-8") as arquivo:
        
            for i,linha in enumerate(arquivo):
                print(linha)
    print('-------------------')