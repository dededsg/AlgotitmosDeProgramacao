#3. Elabore um algoritmo que leia do teclado o sexo de uma pessoa. Se o sexo digitado for M ou F, escrever na tela “Sexo
#válido!”. Caso contrário, informar “Sexo inválido!”

sexo = input('digite um sexo válido M ou F: ')

if sexo == 'M' or sexo == 'F' :
    print('sexo válido')
else :
    print('sexo não válido')

