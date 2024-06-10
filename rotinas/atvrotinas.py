num  = int(input('escreva um numero positivo maior que zero: '))
result = num
for i in range(0, num, 1):
    result = i + result
    
print(f'a soma é {result}')


def somatorio(num):
    if num <= 0:
        return 0
    return num + somatorio(num-1) #chama a função novamente com n-1  

num  = int(input('escreva um numero positivo maior que zero: '))
print(f'o resultado do somatorio do número até {num} é: {somatorio(num)}')




    
    

