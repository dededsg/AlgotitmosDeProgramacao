'''
1. Crie um registro chamado Carro, que possui uma variável chamada ano, do tipo inteiro, uma variável chamada
quilometragem, também do tipo inteiro, e uma variável do tipo caractere para armazenar o modelo:
a. Crie um vetor do registro chamado Carro
b. No registro do 1º elemento do vetor, armazene os seguintes atributos do carro:
i. Ano: 2013
ii. Quilometragem: 50000
iii. Modelo: Prisma
2. Dado que para cada aluno de uma turma de 10 alunos se tenha: número de matrícula, nome e média final, faça
um algoritmo que:
Imprime o nome e a média final de cada aluno;
Imprime a média geral da turma;
'''
#ATV1:

class Carro:
    def __init__(self, ano, quilometragem, modelo):
        self.ano = ano
        self.quilometragem = quilometragem
        self.modelo = modelo

vetor_carros = []

carro1 = Carro(2013, 50000, 'Prisma')
vetor_carros.append(carro1)

print(f"Ano: {vetor_carros[0].ano}")
print(f"Quilometragem: {vetor_carros[0].quilometragem}")
print(f"Modelo: {vetor_carros[0].modelo}")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#ATV2:

class Aluno:
    def __init__(self, numero_matricula, nome, media_final):
        self.numero_matricula = numero_matricula
        self.nome = nome
        self.media_final = media_final
        
turma = []

turma.append(Aluno(1, 'Ana', 7.5))
turma.append(Aluno(2, 'Bruno', 8.0))
turma.append(Aluno(3, 'Carlos', 9.0))
turma.append(Aluno(4, 'Diana', 6.5))
turma.append(Aluno(5, 'Eduardo', 7.0))
turma.append(Aluno(6, 'Fernanda', 8.5))
turma.append(Aluno(7, 'Gustavo', 5.5))
turma.append(Aluno(8, 'Helena', 9.5))
turma.append(Aluno(9, 'Igor', 6.0))
turma.append(Aluno(10, 'Julia', 8.0))

print("Nome e média final de cada aluno:")
for aluno in turma:
    print(f"Nome: {aluno.nome}, Média Final: {aluno.media_final}")

soma_medias = sum(aluno.media_final for aluno in turma)
media_geral = soma_medias / len(turma)
print(f"\nMédia geral da turma: {media_geral:.2f}")







