alunos = [
    {'nome': 'Develin', 'notas' : [8, 10, 10]},
    {'nome': 'Joca', 'notas' : [7, 9, 3]},
    {'nome': 'Coca', 'notas' : [8, 10, 5]}
]

def calcula(notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += nota
    media = totalNotas / len(notas)
    
    return media

for aluno in alunos:
    nome = aluno['nome'] # chave dicionario aluno
    notas = aluno['notas']
    
    media = calcula(notas)
    print(f'A média do(a) {nome} é: {media}')
    
##############################################################
    
def soma(a,b,c):
    print(f'A soma é {a+b+c}')
soma(1,2,3)

###########################################################

#packing - multiplos parametros

def somar2(*numeros):
    print(type(numeros))
    total = 0
    for num in numeros:
        total += num
    print(total)
    
somar2(10,20,31,20,12,32,15,589,49,598,456,6,484,4,4,4,894,84,894)

############################################################

#unpacking - multiplos parametros

def somar3(numero1, numero2):
    somar = numero1 + numero2
    print(f'Total: {somar}')

num = [10, 5]
somar3(*num)

#parametro opicional
def calcular_media2(nota1, nota2, ponto_extra=0, kahoot=0):
    media = (nota1 + nota2)/2 + ponto_extra
    print(f'Média: {media} e mais ponto extra da patifaria vulgo kahoot {kahoot}')
    
calcular_media2(9, 8, kahoot = 1)

# função anonima / expressão lambda

subtrair = lambda a, b : a - b
print(subtrair(5,2))

mult = lambda a, b : print(f'Resultado: {a * b}')
mult(1,2)

##########################################################

