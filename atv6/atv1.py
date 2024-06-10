def verifica(num):
    if num > 0 and num < 10:
        print ("está entre 0 e 10")
    else:
        print ("não está entre 0 e 10")
        
num = float(input('digite um valor'))
print(verifica(num))