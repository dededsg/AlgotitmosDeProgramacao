#4. Faça a implementação de uma calculadora no VisuAlg. Considere que o usuário deve informar a
#operação desejada e 2 números inteiros. Implemente os procedimentos e funções para:
#- Mostrar o menu (selecionar opção);
#- Somar;
#- Subtrair;
#- Multiplicar;
#- Dividir.

def soma(num1, num2):
    return num1 + num2
def subtrair(num1, num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    return num1 / num2

print("++++++++++++++++++++++++++++++++++++++")
print("CALCULADORA")
print("++++++++++++++++++++++++++++++++++++++")

operacao = input("Digite a operação (somar, subtrair, multiplicar, dividir): ")
num1 = float(input("Digite o primerio valor: "))
num2 = float(input("Digite o segundo valor: "))

if operacao.lower() == "somar":
    print(soma(num1,num2))
    
elif operacao.lower() == "subtrair":
    print(subtrair(num1,num2))
    
elif operacao.lower() == "multiplicar":
    print(multiplicar(num1,num2))
    
elif operacao.lower() == "dividir":
    print(dividir(num1,num2))
else:
    print("++++ERROR+++++")
    print("Operação matemática inválida")
    print("++++ERROR+++++")
    
