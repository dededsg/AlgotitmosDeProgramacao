#5. Elabore um algoritmo a ler 4 notas de um aluno (de 0 a 10). Após calcular a média das notas, apresentar a mensagem
#“Aprovada” se o aluno tiver obtido média maior ou igual a 6, caso contrário, apresentar “Reprovado”.

nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
nota3 = float(input("digite a nota 3: "))
nota4 = float(input("digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 6 :
    print("Aprovado")
else :
    print("Reprovado")
