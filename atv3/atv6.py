#6. Altere o algoritmo anterior para que seja lido do teclado, além das notas, o sexo do aluno (M ou F). Se for masculino, o
#resultado deverá ser precedido de “Caro aluno, seu resultado é: “. Se for feminino, o resultado deverá ser precedido de
#“Cara aluna, seu resultado é: “.+


nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
nota3 = float(input("digite a nota 3: "))
nota4 = float(input("digite a nota 4: "))
sexo = input("digite um sexo do aluno M ou F: ")

media = (nota1 + nota2 + nota3 + nota4)/4

if sexo == "M" :
    txt = "Caro aluno"
else :
    txt = "Cara aluna"


if media >= 6 :
    print(txt,", seu resultado é: Aprovado")
else :
    print(txt,", seu resultado é: Reprovado")
