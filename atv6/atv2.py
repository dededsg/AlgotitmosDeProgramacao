def menor(num1,num2,num3):
    menorL = min(num1,num2,num3)
    return menorL

def maior(num1,num2,num3):
    menorM = max(num1,num2,num3)
    return menorM
    
num1 = float(input('digite um valor'))
num2 = float(input('digite um valor'))
num3 = float(input('digite um valor'))

print("Menor número",menor(num1, num2,num3))
print("Maior número",maior(num1, num2,num3))

result = maior(num1, num2, num3)
print(result)