#Crie um programa que lê um número não-negativo (> 0) do usuário, e calcula a operação fatorial
#para aquele número.
#- Com estruturas de repetição (PARA, ENQUANTO...)
#- Com chamadas recursivas
#- OBS: Fatorial de 5 -> 5! = 5 * 4 * 3 * ... * 2 * 1


def fatorial(num: int) -> int:
    result = 1
    for i in range(num, 0, -1):
        print(i)
        result = result * i 
    return result

num = int(input("Digite um valor inteiro maior que 0: "))

print(fatorial(num) if num > 0 else "Digite um valor maior que ZERO!")